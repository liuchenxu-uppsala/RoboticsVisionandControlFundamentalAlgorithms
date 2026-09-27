"""
6.6 Sequential Monte-Carlo Localization —— 粒子滤波定位demo
不需要假设高斯分布, 用一大群'候选位姿'去逼近真实的概率分布
"""
import numpy as np
import matplotlib.pyplot as plt
from roboticstoolbox import Bicycle, RandomPath, LandmarkMap, RangeBearingSensor, ParticleFilter
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
matplotlib.rcParams['axes.unicode_minus'] = False   # 防止负号也显示成方块
matplotlib.use('TkAgg')   # 强制用TkAgg这个后端,绕开Wayland的兼容性问题
np.random.seed(0)
map = LandmarkMap(20, workspace=10)

V = np.diag([0.02, np.deg2rad(0.5)]) ** 2
robot = Bicycle(covar=V, animation="car", workspace=map)
robot.control = RandomPath(workspace=map)
robot.init()

W = np.diag([0.1, np.deg2rad(1)]) ** 2
sensor = RangeBearingSensor(robot, map, covar=W, plot=True)

# Q: 每一步预测阶段, 加给每个粒子的随机扰动的协方差(让粒子群'发散探索')
Q = np.diag([0.1, 0.1, np.deg2rad(1)]) ** 2
# L: 似然函数里用的协方差(决定'差多少分算差很多')
L = np.diag([0.1, 0.1])

pf = ParticleFilter(robot, sensor=sensor, R=Q, L=L, nparticles=1000)
pf.run(T=10)

plt.figure(figsize=(8, 8))
map.plot()
robot.plot_xy(color="b")     # 真实轨迹
pf.plot_xy(color="r")        # 粒子滤波估计出来的轨迹(粒子群的加权平均)
plt.title("粒子滤波定位: 1000个粒子逐渐收敛到真实位姿附近")
plt.savefig("particle_filter_localization.png", dpi=150)
plt.show()

# 看粒子群的'发散程度'(标准差)随时间怎么变 -- 应该先高后低,收敛过程
plt.figure()
plt.plot(pf.get_std()[:100, :])
plt.legend(["x的标准差", "y的标准差", "theta的标准差(x10)"])
plt.xlabel("时间步")
plt.title("粒子群标准差随时间下降: 一开始不确定, 逐渐收敛")
plt.savefig("particle_filter_std.png", dpi=150)
plt.show()

# 直接看粒子群本身长什么样(概率密度的离散近似)
pf.plot_pdf()
plt.show()