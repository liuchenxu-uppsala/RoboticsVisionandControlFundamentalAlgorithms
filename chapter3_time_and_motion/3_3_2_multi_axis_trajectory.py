"""
3.3.2 - Multi-Axis Trajectories 练习
"""

import numpy as np
from roboticstoolbox import mtraj, trapezoidal, quintic
t = np.linspace(0,1,50)
# 2轴例子:轴1从0到1,轴2从2到-1
traj = mtraj(quintic,[0,2],[1,-1],50)
print("轨迹形状:", traj.q.shape)

# 起点位置 终点位置 打印出来
print("起点位置",traj.q[0])
print("终点位置",traj.q[-1])
# 取出单独一个轴的曲线
axis1 = traj.q[:,0]
axis2 = traj.q[:,1]
print("轴1的轨迹(前5个点):", axis1[:5])
print("轴2的轨迹(前5个点):", axis2[:5])