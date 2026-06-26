import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# =========================================================================
# 渲染环境配置（全局绑定 Times New Roman + STIX 数学字体，中英文分离）
# =========================================================================
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
plt.rcParams["axes.unicode_minus"] = False

zh_prop_title = fm.FontProperties(
    family=["Microsoft YaHei", "SimHei", "SimSun"],
    weight="black",
    size=34
)
zh_prop_label = fm.FontProperties(
    family=["Microsoft YaHei", "SimHei", "SimSun"],
    weight="black",
    size=28
)
zh_prop_legend = fm.FontProperties(
    family=["Microsoft YaHei", "SimHei", "SimSun"],
    weight="bold",
    size=22
)

# =========================================================================
# 1. 构造一维真实模型与病态正演算子
# =========================================================================
np.random.seed(42)

n = 160
grid = np.linspace(0.0, 1.0, n)

x_true = (
    0.8 * np.exp(-0.5 * ((grid - 0.30) / 0.055) ** 2)
    + 1.0 * np.exp(-0.5 * ((grid - 0.68) / 0.075) ** 2)
)
x_true /= np.max(x_true)

sigma_blur = 0.035
forward_matrix = np.exp(
    -0.5 * ((grid[:, None] - grid[None, :]) / sigma_blur) ** 2
)
forward_matrix /= forward_matrix.sum(axis=1, keepdims=True)

# =========================================================================
# 2. 生成含噪观测数据 y = A x + eta
# =========================================================================
y_clean = forward_matrix @ x_true

noise_level = 0.01
noise = noise_level * np.linalg.norm(y_clean) / np.sqrt(n) * np.random.randn(n)
y_noisy = y_clean + noise

# =========================================================================
# 3. 直接伪逆反演与 Tikhonov 正则化反演
# =========================================================================
x_pinv = np.linalg.pinv(forward_matrix, rcond=1e-4) @ y_noisy

alpha = 2e-3
normal_matrix = forward_matrix.T @ forward_matrix
right_hand_side = forward_matrix.T @ y_noisy
x_tikhonov = np.linalg.solve(
    normal_matrix + alpha * np.eye(n),
    right_hand_side
)

# =========================================================================
# 4. 计算奇异值、条件数与重构误差
# =========================================================================
singular_values = np.linalg.svd(forward_matrix, compute_uv=False)
condition_number = singular_values[0] / singular_values[-1]

relative_noise = np.linalg.norm(noise) / np.linalg.norm(y_clean)
error_pinv = np.linalg.norm(x_pinv - x_true) / np.linalg.norm(x_true)
error_tikhonov = np.linalg.norm(x_tikhonov - x_true) / np.linalg.norm(x_true)

print(f"Condition number of A: {condition_number:.3e}")
print(f"Relative noise level: {relative_noise:.3%}")
print(f"Direct pseudo-inverse error: {error_pinv:.3%}")
print(f"Tikhonov regularization error: {error_tikhonov:.3%}")
print(f"Maximum absolute value of pseudo-inverse solution: {np.max(np.abs(x_pinv)):.3f}")
print(f"Maximum absolute value of Tikhonov solution: {np.max(np.abs(x_tikhonov)):.3f}")

# =========================================================================
# 5. 创建专著级画布与双子图层
# =========================================================================
fig = plt.figure(figsize=(24, 16), dpi=100, facecolor="#FFFFFF")

ax_svd = fig.add_axes([170/2400, 260/1600, 900/2400, 1050/1600])
ax_rec = fig.add_axes([1280/2400, 260/1600, 900/2400, 1050/1600])

# =========================================================================
# 6. 子图（a）：正演算子的奇异值衰减
# =========================================================================
ax_svd.semilogy(
    np.arange(1, n + 1),
    singular_values / singular_values[0],
    color="#003399",
    linewidth=5.0
)

ax_svd.set_title("（a）正演算子的奇异值衰减", fontproperties=zh_prop_title, pad=22)
ax_svd.set_xlabel("奇异值序号", fontproperties=zh_prop_label, labelpad=16)
ax_svd.set_ylabel("归一化奇异值", fontproperties=zh_prop_label, labelpad=16)

ax_svd.grid(True, linestyle="--", linewidth=1.2, alpha=0.45)

# =========================================================================
# 7. 子图（b）：真实模型、直接伪逆与正则化反演结果
# =========================================================================
ax_rec.plot(
    grid,
    x_true,
    color="#003399",
    linewidth=5.0,
    label="真实模型"
)
ax_rec.plot(
    grid,
    x_pinv,
    color="#C62828",
    linewidth=3.5,
    linestyle="--",
    dashes=(6, 4),
    label="直接伪逆"
)
ax_rec.plot(
    grid,
    x_tikhonov,
    color="#2E7D32",
    linewidth=4.5,
    linestyle="-.",
    dashes=(8, 4, 3, 4),
    label="正则化反演"
)

ax_rec.set_title("（b）病态反演中的噪声放大", fontproperties=zh_prop_title, pad=22)
ax_rec.set_xlabel("空间坐标", fontproperties=zh_prop_label, labelpad=16)
ax_rec.set_ylabel("模型幅值", fontproperties=zh_prop_label, labelpad=16)

legend = ax_rec.legend(
    loc="upper right",
    prop=zh_prop_legend,
    framealpha=1.0,
    edgecolor="black",
    borderpad=0.8,
    handlelength=3.0
)
legend.get_frame().set_linewidth(2.5)

# =========================================================================
# 8. 统一加粗边框和刻度
# =========================================================================
for ax in [ax_svd, ax_rec]:
    for spine in ax.spines.values():
        spine.set_linewidth(3.0)
        spine.set_color("#000000")

    ax.tick_params(
        direction="in",
        length=16,
        width=3,
        colors="#000000",
        bottom=True,
        top=True,
        left=True,
        right=True
    )

    for tick in ax.get_xticklabels() + ax.get_yticklabels():
        tick.set_fontsize(22)
        tick.set_fontweight("black")

plt.show()
