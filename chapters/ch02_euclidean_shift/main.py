import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from scipy.stats import norm

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
    size=28
)
zh_prop_label = fm.FontProperties(
    family=["Microsoft YaHei", "SimHei", "SimSun"],
    weight="black",
    size=22
)
zh_prop_legend = fm.FontProperties(
    family=["Microsoft YaHei", "SimHei", "SimSun"],
    weight="bold",
    size=18
)

# =========================================================================
# 1. 构造一维参考信号与空间平移信号
# =========================================================================
n_bins = 2001
grid = np.linspace(-10.0, 10.0, n_bins)

source_pos = 0.0
sigma = 1.0

reference_signal = norm.pdf(grid, loc=source_pos, scale=sigma)
reference_signal /= np.sum(reference_signal)

shift_test = 2.5
shifted_signal = norm.pdf(grid, loc=source_pos + shift_test, scale=sigma)
shifted_signal /= np.sum(shifted_signal)

# =========================================================================
# 2. 计算逐点欧氏残差与单点错位损失
# =========================================================================
residual = shifted_signal - reference_signal

l2_squared_loss = np.sum(residual ** 2)
l1_residual_mass = np.sum(np.abs(residual))

positive_peak_position = grid[np.argmax(residual)]
negative_peak_position = grid[np.argmin(residual)]

print(f"--- 空间错位量 (Spatial Shift) s = {shift_test:.1f} ---")
print(f"L2 squared loss: {l2_squared_loss:.8f}")
print(f"L1 residual mass: {l1_residual_mass:.6f}")
print(f"Positive residual peak near x = {positive_peak_position:.2f}")
print(f"Negative residual peak near x = {negative_peak_position:.2f}")
print("-" * 40)

# =========================================================================
# 3. 扫描不同空间错位量下的欧氏失配地形
# =========================================================================
shift_values = np.linspace(-6.0, 6.0, 121)
l2_landscape = []

print("正在计算欧氏失配随空间错位变化的地形图，请稍候...")
for shift in shift_values:
    predicted_signal = norm.pdf(grid, loc=source_pos + shift, scale=sigma)
    predicted_signal /= np.sum(predicted_signal)

    loss_value = np.sum((predicted_signal - reference_signal) ** 2)
    l2_landscape.append(loss_value)

l2_landscape = np.array(l2_landscape)

# =========================================================================
# 4. 创建专著级三联子图画布
# =========================================================================
fig = plt.figure(figsize=(24, 16), dpi=100, facecolor="#FFFFFF")

# 增大三个子图之间的间距，避免 y 轴标签和相邻图层重叠
ax_signal = fig.add_axes([105/2400, 300/1600, 560/2400, 980/1600])
ax_resid = fig.add_axes([890/2400, 300/1600, 560/2400, 980/1600])
ax_land = fig.add_axes([1675/2400, 300/1600, 560/2400, 980/1600])

# =========================================================================
# 5. 子图（a）：参考信号与平移信号
# =========================================================================
ax_signal.plot(
    grid,
    reference_signal,
    color="#003399",
    linewidth=5.0,
    label="参考信号"
)
ax_signal.plot(
    grid,
    shifted_signal,
    color="#C62828",
    linewidth=4.5,
    linestyle="--",
    dashes=(6, 4),
    label="平移信号"
)

ax_signal.set_title("（a）空间平移信号", fontproperties=zh_prop_title, pad=22)
ax_signal.set_xlabel("空间坐标", fontproperties=zh_prop_label, labelpad=14)
ax_signal.set_ylabel("归一化幅值", fontproperties=zh_prop_label, labelpad=18)

legend_signal = ax_signal.legend(
    loc="upper right",
    prop=zh_prop_legend,
    framealpha=1.0,
    edgecolor="black",
    borderpad=0.7,
    handlelength=2.8
)
legend_signal.get_frame().set_linewidth(2.2)

# =========================================================================
# 6. 子图（b）：逐点残差结构
# =========================================================================
ax_resid.plot(
    grid,
    residual,
    color="#003399",
    linewidth=5.0
)
ax_resid.axhline(
    0.0,
    color="#000000",
    linewidth=2.5,
    linestyle="-"
)

ax_resid.set_title("（b）逐点欧氏残差", fontproperties=zh_prop_title, pad=22)
ax_resid.set_xlabel("空间坐标", fontproperties=zh_prop_label, labelpad=14)
ax_resid.set_ylabel("平移信号 $-$ 参考信号", fontproperties=zh_prop_label, labelpad=28)

# =========================================================================
# 7. 子图（c）：欧氏失配随空间错位变化的地形
# =========================================================================
ax_land.plot(
    shift_values,
    l2_landscape,
    color="#003399",
    linewidth=5.0
)

ax_land.scatter(
    [shift_test],
    [l2_squared_loss],
    s=160,
    color="#C62828",
    edgecolor="#000000",
    linewidth=2.0,
    zorder=5
)

ax_land.set_title("（c）欧氏失配地形", fontproperties=zh_prop_title, pad=22)
ax_land.set_xlabel("空间错位量", fontproperties=zh_prop_label, labelpad=14)
ax_land.set_ylabel(r"$L^2$ 平方损失", fontproperties=zh_prop_label, labelpad=30)

# =========================================================================
# 8. 统一加粗边框和刻度
# =========================================================================
for ax in [ax_signal, ax_resid, ax_land]:
    for spine in ax.spines.values():
        spine.set_linewidth(3.0)
        spine.set_color("#000000")

    ax.tick_params(
        direction="in",
        length=15,
        width=3,
        colors="#000000",
        bottom=True,
        top=True,
        left=True,
        right=True
    )

    for tick in ax.get_xticklabels() + ax.get_yticklabels():
        tick.set_fontsize(19)
        tick.set_fontweight("black")

plt.show()
