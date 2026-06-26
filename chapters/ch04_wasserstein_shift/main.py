import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import ot  # POT: Python Optimal Transport
from scipy.stats import norm

# =========================================================================
# 1. 渲染环境配置（全局绑定 Times New Roman + STIX 数学字体，中英文分离）
# =========================================================================
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
plt.rcParams["axes.unicode_minus"] = False

zh_prop_legend = fm.FontProperties(
    family=["Microsoft YaHei", "SimHei", "SimSun"],
    weight="black",
    size=32
)
zh_prop_axis = fm.FontProperties(
    family=["Microsoft YaHei", "SimHei", "SimSun"],
    weight="black",
    size=42
)
zh_prop_tick = fm.FontProperties(
    family=["Microsoft YaHei", "SimHei", "SimSun"],
    weight="black",
    size=36
)

# =========================================================================
# 2. 物理系统初始化（3001 个点，降低插值误差）
# =========================================================================
n_bins = 3001
x = np.linspace(-15, 15, n_bins)
source_pos, sigma = 0.0, 1.0

y_true = norm.pdf(x, loc=source_pos, scale=sigma)
y_true /= np.sum(y_true)

# 提取单点 s=4.0 进行精确验证
s_shift_test = 4.0
y_pred_test = norm.pdf(x, loc=source_pos + s_shift_test, scale=sigma)
y_pred_test /= np.sum(y_pred_test)

mse_test = np.sum((y_pred_test - y_true) ** 2)
w1_test = ot.wasserstein_1d(x, x, y_pred_test, y_true, p=1)
w2_sq_test = ot.wasserstein_1d(x, x, y_pred_test, y_true, p=2)

print(f"--- 空间错位量 (Phase Shift) s = {s_shift_test:.1f} ---")
print(f"L2 (MSE) Loss: {mse_test:.6f}")
print(f"W1 Loss (Linear): {w1_test:.6f}")
print(f"W2^2 Loss (Quadratic): {0.5 * w2_sq_test:.6f}")
print("-" * 40)

# =========================================================================
# 3. 连续扫描计算地形图（201 个点）
# =========================================================================
shifts = np.linspace(-8, 8, 201)
loss_mse, loss_w1, loss_w2 = [], [], []

print("正在计算全局泛函能量地形图，请稍候...")
for s in shifts:
    y_pred = norm.pdf(x, loc=source_pos + s, scale=sigma)
    y_pred /= np.sum(y_pred)

    loss_mse.append(np.sum((y_pred - y_true) ** 2))
    loss_w1.append(ot.wasserstein_1d(x, x, y_pred, y_true, p=1))
    loss_w2.append(0.5 * ot.wasserstein_1d(x, x, y_pred, y_true, p=2))

# 归一化地形形状
loss_mse_norm = np.array(loss_mse) / np.max(loss_mse)
loss_w1_norm = np.array(loss_w1) / np.max(loss_w1)
loss_w2_norm = np.array(loss_w2) / np.max(loss_w2)

# =========================================================================
# 4. 创建专著级画布与封闭轴图层
# =========================================================================
fig = plt.figure(figsize=(24, 16), dpi=100, facecolor="#FFFFFF")

# 图表区域：X 向占用 1850 px，Y 向占用 1200 px
ax_data = fig.add_axes([300/2400, 300/1600, 1850/2400, 1200/1600])

# 绘制三条泛函能量曲线
ax_data.plot(
    shifts,
    loss_mse_norm,
    color="#C62828",
    lw=8,
    zorder=4,
    label=r"传统 $L_2$ 范数 ($MSE$)"
)
ax_data.plot(
    shifts,
    loss_w1_norm,
    color="#003399",
    lw=6,
    ls="--",
    dashes=(6, 4),
    zorder=5,
    label=r"$1$-Wasserstein ($W_1$) 距离"
)
ax_data.plot(
    shifts,
    loss_w2_norm,
    color="#2E7D32",
    lw=6,
    ls="-.",
    dashes=(8, 4, 3, 4),
    zorder=6,
    label=r"$2$-Wasserstein ($W_2$) 代价"
)

ax_data.set_xlim(-8, 8)
ax_data.set_ylim(0, 1.05)

# 封闭轴与内向刻度系统
for spine in ax_data.spines.values():
    spine.set_linewidth(3.0)
    spine.set_color("#000000")

ax_data.tick_params(
    direction="in",
    length=20,
    width=3,
    colors="#000000",
    bottom=True,
    top=True,
    left=True,
    right=True,
    labelbottom=False,
    labelleft=False
)

ax_data.set_xticks([-8, -4, 0, 4, 8])
ax_data.set_yticks([0, 0.5, 1.0])

legend = ax_data.legend(
    loc="upper center",
    prop=zh_prop_legend,
    framealpha=1.0,
    edgecolor="black",
    borderpad=0.8,
    handlelength=3.0
)
legend.get_frame().set_linewidth(2.5)

# =========================================================================
# 5. 全局标注层 ax_main
# =========================================================================
ax_main = fig.add_axes([0, 0, 1, 1])
ax_main.set_xlim(0, 2400)
ax_main.set_ylim(0, 1600)
ax_main.axis("off")
ax_main.set_zorder(100)

def draw_text(x_pos, y_pos, text, size, color="#000000", align="center", rotation=0):
    if any("\u4e00" <= char <= "\u9fff" for char in text):
        font_prop = fm.FontProperties(
            family=["Microsoft YaHei", "SimHei", "SimSun"],
            weight="black",
            size=size
        )
        ax_main.text(
            x_pos,
            y_pos,
            text,
            ha=align,
            va="center",
            color=color,
            fontproperties=font_prop,
            rotation=rotation
        )
    else:
        ax_main.text(
            x_pos,
            y_pos,
            text,
            ha=align,
            va="center",
            fontsize=size,
            color=color,
            fontweight="black",
            rotation=rotation
        )

# --- 坐标轴外部刻度标签 ---
# X 轴刻度（物理映射位置：-8 在 300，0 在 1225，8 在 2150）
draw_text(300, 200, r"$-8$", 36)
draw_text(762, 200, r"$-4$", 36)
draw_text(1225, 200, r"$0$", 36)
draw_text(1688, 200, r"$4$", 36)
draw_text(2150, 200, r"$8$", 36)

# Y 轴刻度（物理映射位置：0.0 在 300，0.5 在 871，1.0 在 1443）
draw_text(220, 300, r"$0.0$", 36)
draw_text(220, 871, r"$0.5$", 36)
draw_text(220, 1443, r"$1.0$", 36)

# --- 坐标轴标题 ---
draw_text(1225, 80, r"空间相位错位参数 $s$", 42)
draw_text(80, 900, "归一化泛函能量", 42, rotation=90)

plt.show()
