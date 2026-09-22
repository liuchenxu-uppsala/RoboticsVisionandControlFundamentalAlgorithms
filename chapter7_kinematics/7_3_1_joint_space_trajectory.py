"""
7.3.1 - Joint-Space Motion 练习
"""
import numpy as np
from roboticstoolbox import models, jtraj
from spatialmath import SE3
puma = models.DH.Puma560()
# 起点和终点位姿(位置不同,姿态也不同) 
# 0.4, -0.2, 0 3rad
# 0.4, 0.2, 0 1rad
start = SE3.Trans(0.4, -0.2, 0) * SE3.Rx(3)
end = SE3.Trans(0.4, 0.2, 0) * SE3.Rx(1)

# 各自求解析解IK(指定右手、肘部朝上,保证两个解连贯)
sol1 = puma.ik_LM(start,"ru")
sol2 = puma.ik_LM(end,"ru")
print("起点关节角度:", sol1.q)
print("终点关节角度:", sol2.q)


# 时间序列:2秒,每20毫秒一个点
t = np.arange(0,10,0.02)
print("总共多少个时间点:", len(t))

# 生成关节空间轨迹(五次多项式插值)
traj = jtraj(sol1.q,sol2.q,t)
print("\n轨迹位置数组形状:", traj.q.shape)
print("轨迹速度数组形状:", traj.qd.shape)
print("轨迹加速度数组形状:", traj.qdd.shape)


# 验证:起点和终点,速度、加速度应该都接近0(平滑启停)
print("起始速度:",traj.qd[0],"开始加速度:",traj.qdd[0])
print()
print("开始加速度:",traj.qd[-1],"结束加速度:",traj.qdd[-1])

# 中间某个时间点,速度应该明显不是0(正在运动中)
middle = len(t)//2
print("中间速度:",traj.qd[middle],"中间加速度:",traj.qdd[middle])
print()
# 可视化(需要图形界面支持)
puma.plot(traj.q)
