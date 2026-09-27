"""
6.3 Creating a Landmark Map —— 反过来:机器人位姿已知,估计路标位置
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
robot = Bicycle(covar=V, animation="car")
robot.control = RandomPath(workspace=map)
robot.init()

W = np.diag([0.1, np.deg2rad(1)]) ** 2
sensor = RangeBearingSensor(robot=robot, map=map, covar=W,
                             range=4, angle=[-np.pi/2, np.pi/2], animate=True)

# 关键区别: robot=(robot, None) —— None表示"假设机器人位姿完美已知,不用估计"
# 也没有传P0(机器人位姿部分),因为状态向量一开始是空的(M=0,没见过任何路标)
# 也没有传map(建图问题里,map对EKF来说是未知的,这正是要估计的东西)
ekf = EKF(robot=(robot, None), sensor=(sensor, W))
ekf.run(T=100)

plt.figure(figsize=(8, 8))
map.plot()              # 真实路标位置
ekf.plot_map()           # EKF估计出来的路标位置 + 置信椭圆
robot.plot_xy()          # 机器人真实路径(因为假设位姿已知,这条路径就是"真值")
plt.title("6.3 建图: 路标位置估计, 置信椭圆应该都很小")
plt.savefig("ekf_mapping.png", dpi=150)
plt.show()

# 看某个具体路标估计得怎么样,比如10号路标
idx, count = ekf.landmark(10)
print(f"10号路标是第{idx}个被看到的,总共被观测了{count}次")
print("10号路标估计坐标:", ekf.x_est[idx*2:idx*2+2])
print("真实坐标:", map[10])
print("10号路标估计协方差:\n", ekf.P_est[idx*2:idx*2+2, idx*2:idx*2+2])