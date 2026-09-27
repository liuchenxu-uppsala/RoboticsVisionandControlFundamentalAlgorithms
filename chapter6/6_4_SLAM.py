"""
6.4 SLAM —— 位姿和地图都未知,同时估计
"""
import numpy as np
import matplotlib.pyplot as plt
from roboticstoolbox import Bicycle, RandomPath, EKF, LandmarkMap, RangeBearingSensor
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
matplotlib.rcParams['axes.unicode_minus'] = False   # 防止负号也显示成方块
matplotlib.use('TkAgg')   # 强制用TkAgg这个后端,绕开Wayland的兼容性问题
np.random.seed(0)
map = LandmarkMap(20, workspace=10)

V = np.diag([0.02, np.deg2rad(0.5)]) ** 2
# 故意设一个跟原点差很远的初始位姿,凸显"SLAM坐标系跟世界坐标系对不上"这件事
robot = Bicycle(covar=V, x0=(3, 6, np.deg2rad(-45)), animation="car")
robot.control = RandomPath(workspace=map)
robot.init()

W = np.diag([0.1, np.deg2rad(1)]) ** 2
sensor = RangeBearingSensor(robot=robot, map=map, covar=W,
                             range=4, angle=[-np.pi/2, np.pi/2], animate=True)

P0 = np.diag([0.05, 0.05, np.deg2rad(0.5)]) ** 2   # 只有机器人位姿部分的初始协方差,路标还是M=0
# 注意: 跟6.3不一样,这里robot=(robot, V)传的是真实V(需要估计位姿了);
#       跟6.2不一样,这里没传map(地图现在也是未知的)
ekf = EKF(robot=(robot, V), P0=P0, sensor=(sensor, W))
ekf.run(T=40)

# ---- 先看"没对齐"的原始结果:世界坐标系里的真值 vs SLAM自己坐标系里的估计 ----
fig, axes = plt.subplots(1, 2, figsize=(14, 7))
plt.sca(axes[0])
map.plot()
robot.plot_xy()
plt.title("真实世界坐标系: 真实路径+真实地图")

plt.sca(axes[1])
ekf.plot_map()
ekf.plot_xy()
ekf.plot_ellipse()
plt.title("SLAM自己的坐标系: 估计路径+估计地图(整体偏移旋转了)")
plt.savefig("slam_before_alignment.png", dpi=150)
plt.show()

# ---- 用至少2个路标的真值vs估计值, 算出对齐变换, 验证SLAM内部的'相对关系'是准的 ----
T = ekf.get_transform(map)
print("SLAM坐标系 -> 世界坐标系 的变换矩阵:\n", T)