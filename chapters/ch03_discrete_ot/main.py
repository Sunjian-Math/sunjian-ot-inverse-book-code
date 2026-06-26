import numpy as np
import ot  # POT: Python Optimal Transport

# =========================================================================
# 1. 构造离散源分布与目标分布
# =========================================================================
source_dist = np.array([0.5, 0.5])
target_dist = np.array([0.2, 0.5, 0.3])

source_coords = np.array([[0.0], [1.0]])
target_coords = np.array([[0.0], [0.5], [1.2]])

# =========================================================================
# 2. 计算二次欧氏代价矩阵并求解离散最优传输计划
# =========================================================================
cost_matrix = ot.dist(source_coords, target_coords, metric="sqeuclidean")
optimal_transport_plan = ot.solve(cost_matrix, source_dist, target_dist).plan

# =========================================================================
# 3. 输出代价矩阵与最优传输矩阵
# =========================================================================
print("Cost Matrix c(x,y): \n", cost_matrix)
print("Optimal Transport Plan (\\pi^*): \n", optimal_transport_plan)
