"""
7.3.2 - Cartesian Motion,对比关节空间 vs 笛卡尔空间轨迹
"""

import numpy as np
from roboticstoolbox import models, jtraj, ctraj
from spatialmath import SE3
import matplotlib.pyplot as plt

# 起点和终点位姿(位置不同,姿态也不同) 
# 0.4, -0.2, 0 3rad
# 0.4, 0.2, 0 1rad
puma = models.DH.Puma560()
start = SE3.Trans(0.4, -0.2, 0) * SE3.Rx(3)
end = SE3.Trans(0.4, 0.2, 0) * SE3.Rx(1)
# 方法一:关节空间插值
sol1 = puma.ikine_a(start,"ru")
sol2 = puma.ikine_a(end,"ru")
t = np.arange(0,2,0.02)
traj_joint = jtraj(sol1.q,sol2.q,t)
# 方法二:笛卡尔空间插值


TES = ctraj(start,end,t)
traj_cart = puma.ikine_a(TES)

# 对比:把两种方法,各自的关节角度,重新代入FK,看末端实际走的路径
positions_joint = np.array([puma.fkine(q).t for q in traj_joint.q])
positions_cart = np.array([puma.fkine(q).t for q in traj_cart.q])

# 画出末端在xy平面的路径,对比形状
plt.figure()
plt.plot(positions_joint[:, 0], positions_joint[:, 1], label="joint")
plt.plot(positions_cart[:, 0], positions_cart[:, 1], label="cart")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Route VS")
plt.show()

