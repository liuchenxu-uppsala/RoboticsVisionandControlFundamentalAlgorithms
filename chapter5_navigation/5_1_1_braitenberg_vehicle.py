"""
5.1.1 - Braitenberg Vehicle 简化练习
不用bdsim,用普通Python代码模拟"双侧传感器朝光源移动"
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
matplotlib.rcParams['axes.unicode_minus'] = False   # 防止负号也显示成方块
# 光源位置(固定)
light_pos = np.array([10,8])
# 车辆初始状态
x,y = 0,0
# 传感器间距(左右两个虚拟传感器,离车辆中心多远)
sensor_distance = 0.3
# 控制增益 2.0
K = 8.0
# 恒定前进速度 1.0
V = 1
#
dt  = 0.05
steps = 4500
theta = 0
# xs, ys 表示 车辆轨迹
xs , ys = [x],[y]

#传感器的场强
def light_intensity(pos):
    d = np.linalg.norm(pos - light_pos)
    return 1/(d**2 + 0.01)
for _ in range(steps):
    sensor1_position = np.array([x+sensor_distance*np.sin(theta),y-sensor_distance*np.cos(theta)])
    sensor2_position = np.array([x-sensor_distance*np.sin(theta),y+sensor_distance*np.cos(theta)])
    light1_strenth = light_intensity(sensor1_position)
    light2_strenth = light_intensity(sensor2_position)
    theta_dot = (light2_strenth - light1_strenth) * K
    v_x = V*np.cos(theta)
    v_y = V*np.sin(theta)
    xs.append(x)
    ys.append(y)
    x = x + dt * v_x
    y = y + dt * v_y
    theta  = theta + dt * theta_dot
# 左右两个传感器的位置(垂直于车头方向,左右各偏移sensor_offset)
# 读取左右传感器的场强
# Braitenberg核心逻辑:左右读数的差值,直接驱动转向
# 更新状态(用我们第4章学过的差速驱动运动学方程)


# 可视化
plt.figure(figsize=(6, 6))
plt.plot(xs, ys, 'b-', label='车辆轨迹')
plt.plot(light_pos[0], light_pos[1], 'y*', markersize=20, label='光源')
plt.plot(xs[0], ys[0], 'go', label='起点')
plt.axis('equal')
plt.legend()
plt.title('Braitenberg车辆:靠双侧传感器,朝光源移动')
plt.grid(True)
plt.show()