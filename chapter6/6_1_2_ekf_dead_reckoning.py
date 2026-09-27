"""
6.1 Dead Reckoning Using Odometry —— EKF预测(无观测修正)演示
对应书中 6.1.2 节:只有 predict,没有 correct/update,纯航位推算
"""

import numpy as np
import matplotlib.pyplot as plt
from roboticstoolbox import Bicycle, RandomPath, EKF
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
matplotlib.rcParams['axes.unicode_minus'] = False   # 防止负号也显示成方块
matplotlib.use('TkAgg')   # 强制用TkAgg这个后端,绕开Wayland的兼容性问题

V = np.diag([0.02, np.deg2rad(0.5)]) ** 2
print("里程计噪声协方差 V =\n", V)

robot = Bicycle(covar=V, animation="car")
robot.control = RandomPath(workspace=10)   # 随机走位,不用手动指定目标点
robot.init()

P0 = np.diag([0.05, 0.05, np.deg2rad(0.5)]) ** 2
ekf = EKF(robot=(robot, V), P0=P0)

ekf.run(T=20)

robot.plot_xy(color="b")       # 蓝色:仿真产生的"真实"运动轨迹(带真实噪声)
ekf.plot_xy(color="r")         # 红色:EKF纯靠里程计积分估计出来的轨迹
ekf.plot_ellipse(filled=True, facecolor="g", alpha=0.3)  # 每隔几步画一个95%置信椭圆
plt.legend(["真实轨迹", "估计轨迹", "95%置信椭圆"])
plt.title("Dead Reckoning: 蓝红两条线会越走越分开,绿色椭圆会越来越大")
plt.savefig("ekf_dead_reckoning.png", dpi=150)
plt.show()
Pnorm = ekf.get_Pnorm()
print(type(Pnorm), len(Pnorm))
print(Pnorm[:5])