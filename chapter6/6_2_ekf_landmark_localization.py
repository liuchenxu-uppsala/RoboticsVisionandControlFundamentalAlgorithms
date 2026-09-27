"""
6.2 Localizing with a Landmark Map —— 完整EKF定位demo(预测+观测修正)
对比6.1节纯dead reckoning的demo,这里多了地图(map)和传感器(sensor)两样东西,
EKF不再只会predict,还会在测到路标时做correct(修正)。
"""
import numpy as np
import matplotlib.pyplot as plt
from roboticstoolbox import Bicycle, RandomPath, EKF, LandmarkMap, RangeBearingSensor
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
matplotlib.rcParams['axes.unicode_minus'] = False   # 防止负号也显示成方块
matplotlib.use('TkAgg')   # 强制用TkAgg这个后端,绕开Wayland的兼容性问题
# ---- 1. 地图:20个已知位置的路标,撒在±10m范围内 ----
np.random.seed(0)
map = LandmarkMap(20, workspace=10)

# ---- 2. 里程计噪声(跟6.1节dead reckoning demo完全一样) ----
V = np.diag([0.02, np.deg2rad(0.5)]) ** 2

# ---- 3. 车 + 随机驾驶员(跟6.1节一样,自动在地图范围内随机绕圈) ----
robot = Bicycle(covar=V, animation="car")
robot.control = RandomPath(workspace=map)
robot.init()

# ---- 4. 新增:测距-测角传感器 ----
# covar=W: 传感器自身的测量噪声,对应式(6.9)里的w
# angle=[-pi/2, pi/2]: 只能看到车头左右各90度范围内的路标
# range=4: 只能看到4米以内的路标
W = np.diag([0.1, np.deg2rad(1)]) ** 2
sensor = RangeBearingSensor(robot=robot, map=map, covar=W,
                             angle=[-np.pi/2, np.pi/2], range=4, animate=True)

# ---- 5. 初始不确定性(跟6.1节一样) ----
P0 = np.diag([0.05, 0.05, np.deg2rad(0.5)]) ** 2

# ---- 6. 建EKF —— 关键区别:这次多传了 map 和 sensor 两个参数 ----
# 有了这两个,EKF每一步除了predict(式6.3/6.4),
# 只要传感器这一步测到了路标,就会自动多做一次correct(式6.10~6.13)
ekf = EKF(robot=(robot, V), P0=P0, map=map, sensor=(sensor, W))

# ---- 7. 跑20秒仿真 ----
ekf.run(T=20)

# ---- 8. 画图:地图 + 真实轨迹 + 估计轨迹 + 置信椭圆 ----
plt.figure(figsize=(8, 8))
#map.plot()               # 黑色星星:20个路标
robot.plot_xy(color="b") # 蓝色:真实轨迹
ekf.plot_xy(color="r")   # 红色:EKF估计轨迹
ekf.plot_ellipse(filled=True, facecolor="g", alpha=0.3)  # 绿色:95%置信椭圆
plt.legend(["真实轨迹", "估计轨迹", "95%置信椭圆(观测到路标时会突然变小)"])
plt.title("EKF定位: 有观测修正 vs 6.1节纯dead reckoning")
plt.savefig("ekf_landmark_localization.png", dpi=150)
plt.show()

# ---- 9. 关键对比:不确定性曲线,应该不再是单调递增了 ----
# Pnorm = ekf.get_Pnorm()
# plt.figure()
# plt.plot(Pnorm)
# plt.xlabel("时间步")
# plt.ylabel("Pnorm = sqrt(det(P))")
# plt.title("有观测修正: 不确定性会在观测到路标时骤降,不再单调递增")
# plt.savefig("pnorm_with_correction.png", dpi=150)
# plt.show()

print("整条曲线是否严格单调递增(跟6.1节demo做对比):",
      np.all(np.diff(Pnorm) > 0))
print("Pnorm最大值:", Pnorm.max(), " 最小值:", Pnorm.min())