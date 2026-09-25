"""
5.4.1 - Distance Transform Path Planning 练习
"""

import numpy as np
from roboticstoolbox import DistanceTransformPlanner
import matplotlib.pyplot as plt

# 6x6 网格,构造一个不规则(L形)障碍物
simplegrid = np.zeros((6, 6))
simplegrid[2:5, 3:5] = 1
simplegrid[3:5, 2] = 1

# 创建距离变换规划器,传入地图
dx = DistanceTransformPlanner(occgrid=simplegrid)

# 规划:告诉它目标位置(x=1, y=1)
dx.plan(goal=(1, 1))

# 可视化距离图(每个格子标出到目标的距离)
dx.plot(labelvalues=True)
plt.show()

# 3D地形图,直观看"下坡滚动"这个比喻
dx.plot_3d()
plt.show()

# 查询一条从(5,4)出发的完整路径
path = dx.query(start=(5, 4))
print("路径:\n", path)
print("总共多少步:", path.shape[0])

# 把路径叠加画在地图上
dx.plot(path)
plt.show()

# 打印本次规划的统计信息(迭代次数、不可达格子数)
dx.plan(goal=(1, 1), summary=True)