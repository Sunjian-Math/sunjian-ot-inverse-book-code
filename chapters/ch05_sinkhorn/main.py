import torch
import time
import math

# =========================================================================
# 1. 底层算子：支持冷启动的无循环 Sinkhorn-Knopp 张量迭代核心
# =========================================================================
def sinkhorn_core(a, b, C, epsilon, num_iters, u_init=None, v_init=None):
    device, dtype = a.device, a.dtype
    u = u_init if u_init is not None else torch.zeros_like(a, dtype=dtype, device=device)
    v = v_init if v_init is not None else torch.zeros_like(b, dtype=dtype, device=device)

    log_a = torch.log(a + 1e-15)
    log_b = torch.log(b + 1e-15)

    for _ in range(num_iters):
        # 算子投影 1：锁定 dim=2 的矩阵-向量对数广播
        M1 = (-C + v.unsqueeze(1)) / epsilon
        max_M1, _ = torch.max(M1, dim=2, keepdim=True)
        sum_exp_M1 = torch.sum(torch.exp(M1 - max_M1), dim=2)
        u = epsilon * (log_a - (torch.log(sum_exp_M1 + 1e-15) + max_M1.squeeze(2)))

        # 算子投影 2：锁定 dim=1 的矩阵-向量对数广播
        M2 = (-C + u.unsqueeze(2)) / epsilon
        max_M2, _ = torch.max(M2, dim=1, keepdim=True)
        sum_exp_M2 = torch.sum(torch.exp(M2 - max_M2), dim=1)
        v = epsilon * (log_b - (torch.log(sum_exp_M2 + 1e-15) + max_M2.squeeze(1)))

    M_final = (-C + u.unsqueeze(2) + v.unsqueeze(1)) / epsilon
    P_optimal = torch.exp(M_final)
    wasserstein_transport_cost = torch.sum(P_optimal * C, dim=(1, 2))

    return torch.mean(wasserstein_transport_cost), u, v


# =========================================================================
# 2. 演进策略：退火逼近与去偏散度
# =========================================================================
def sinkhorn_epsilon_scaling(a, b, C, eps_start=1.0, eps_end=0.005, steps=8, iters_per_step=100):
    eps_schedule = torch.logspace(math.log10(eps_start), math.log10(eps_end), steps)
    u, v = None, None
    for eps in eps_schedule:
        cost, u, v = sinkhorn_core(a, b, C, eps.item(), iters_per_step, u, v)
    return cost


def unbiased_sinkhorn_divergence(a, b, C, epsilon=0.05, num_iters=200):
    W_ab, _, _ = sinkhorn_core(a, b, C, epsilon, num_iters)
    W_aa, _, _ = sinkhorn_core(a, a, C, epsilon, num_iters)
    W_bb, _, _ = sinkhorn_core(b, b, C, epsilon, num_iters)
    return W_ab - 0.5 * (W_aa + W_bb)


# =========================================================================
# 3. 物理系统初始化与算力基准测试
# =========================================================================
def run_benchmark():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    x = torch.linspace(-8, 8, 1000, device=device, dtype=torch.float64)

    # 构造均值错位 Δs = 2.0 的高斯分布，理论解析解 W2^2 = 4.0
    a = torch.exp(-0.5 * (x - 0.0) ** 2)
    a /= a.sum()
    b = torch.exp(-0.5 * (x - 2.0) ** 2)
    b /= b.sum()

    a_batch, b_batch = a.unsqueeze(0), b.unsqueeze(0)
    C_batch = ((x.unsqueeze(1) - x.unsqueeze(0)) ** 2).unsqueeze(0)

    # 预热硬件核心
    _ = sinkhorn_core(a_batch, b_batch, C_batch, 0.1, 10)
    if device.type == "cuda":
        torch.cuda.synchronize()

    # 测算：标准 Sinkhorn
    start = time.perf_counter()
    cost_base, _, _ = sinkhorn_core(a_batch, b_batch, C_batch, epsilon=0.05, num_iters=200)
    if device.type == "cuda":
        torch.cuda.synchronize()
    time_base = (time.perf_counter() - start) * 1000

    # 测算：退火逼近
    start = time.perf_counter()
    cost_anneal = sinkhorn_epsilon_scaling(a_batch, b_batch, C_batch)
    if device.type == "cuda":
        torch.cuda.synchronize()
    time_anneal = (time.perf_counter() - start) * 1000

    # 测算：去偏散度
    start = time.perf_counter()
    cost_unbiased = unbiased_sinkhorn_divergence(a_batch, b_batch, C_batch, epsilon=0.05)
    if device.type == "cuda":
        torch.cuda.synchronize()
    time_unbiased = (time.perf_counter() - start) * 1000

    # 输出学术报告
    print("-----------------------------------------------------------------")
    print(f"{'算法演进路线':<18} | {'测算代价 (W2^2)':<15} | {'相对偏差':<10} | {'前向耗时 (ms)':<10}")
    print("-----------------------------------------------------------------")
    print(f"{'理论解析解':<23} | {'4.00000':<17} | {'0.000%':<10} | {'-':<10}")
    print(f"{'1. 标准 Sinkhorn (ε=0.05)':<19} | {cost_base.item():.5f}           | {abs(cost_base.item() - 4) / 4 * 100:.3f}%     | {time_base:.2f}")
    print(f"{'2. 退火逼近 (ε→0.005)':<19} | {cost_anneal.item():.5f}           | {abs(cost_anneal.item() - 4) / 4 * 100:.3f}%     | {time_anneal:.2f}")
    print(f"{'3. 去偏散度 (ε=0.05)':<20} | {cost_unbiased.item():.5f}           | {abs(cost_unbiased.item() - 4) / 4 * 100:.3f}%     | {time_unbiased:.2f}")
    print("-----------------------------------------------------------------")


if __name__ == "__main__":
    run_benchmark()
