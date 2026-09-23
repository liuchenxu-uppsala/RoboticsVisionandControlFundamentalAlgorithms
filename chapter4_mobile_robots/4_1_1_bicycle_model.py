"""
4.1.1 - Car-Like Vehicle (Bicycle Model) 练习
用运动学方程,模拟车辆绕ICR转圈,验证R_B公式
"""

import numpy as np
import matplotlib.pyplot as plt

# 车辆参数 L=2 v=1 前轮角度是恒定的30度
L = 2.0
V = 1.0
gamma = np.deg2rad(30)

# 理论转弯半径(我们推导的公式)
R_B_theory = L / np.tan(gamma)

print("理论转弯半径 R_B =", R_B_theory)

# 用运动学方程,数值积分,模拟车辆运动 初始化的 从0开始 到 20 step_pace 0.01
x = 0
y = 0
theta = 0
T = 35
dt = 0.01
steps = int(T/dt)
xs, ys = [x], [y]

for _ in range(steps):
    x_vol = V * np.cos(theta)
    y_vol = V * np.sin(theta)
    x = x + x_vol * dt
    y = y + y_vol * dt
    theta = theta + (dt * V * np.tan(gamma)) / L
    xs.append(x)
    ys.append(y)

xs = np.array(xs)
ys = np.array(ys)



center_theory = np.array([0, R_B_theory])
distances = np.sqrt((xs-center_theory[0])**2 + (ys-center_theory[1])**2)
print("最小值:", distances.min())
print("最大值:", distances.max())
print("平均值:", distances.mean())


# 可视化
plt.figure(figsize=(6, 6))
plt.plot(xs, ys, 'b-', label='guijimoni')
plt.plot(center_theory[0], center_theory[1], 'r*', markersize=15, label='ICR')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(f'ICR (L={L}, gamma={np.rad2deg(gamma):.0f}°, R_B={R_B_theory:.2f})')
plt.grid(True)
plt.show()

