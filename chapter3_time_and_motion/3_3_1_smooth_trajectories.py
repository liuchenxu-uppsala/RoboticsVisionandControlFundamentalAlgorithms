"""
3.3.1 - Smooth One-Dimensional Trajectories 练习
对比 quintic(五次多项式) 和 trapezoidal(梯形插值)
"""

import numpy as np
from roboticstoolbox import quintic, trapezoidal
import matplotlib.pyplot as plt
t = np.linspace(0,1,50)
print("第一部分:quintic 五次多项式插值")
traj_q = quintic(0,1,t)
print("起点位置:", traj_q.q[0])
print("终点位置:", traj_q.q[-1])
print("起点速度(应接近0):", traj_q.qd[0])
print("终点速度(应接近0):", traj_q.qd[-1])
print("起点加速度(应接近0):", traj_q.qdd[0])
print("终点加速度(应接近0):", traj_q.qdd[-1])
print("峰值速度:", traj_q.qd.max())
print("速度利用率(平均/峰值):", traj_q.qd.mean() / traj_q.qd.max())



print("第二部分:trapezoidal 梯形插值")
traj_t = trapezoidal(0,1,t)
print("起点位置:", traj_t.q[0])
print("终点位置:", traj_t.q[-1])
print("峰值速度:", traj_t.qd.max())
print("速度利用率(平均/峰值):", traj_t.qd.mean() / traj_t.qd.max())


print("第三部分:非零初始速度导致超调(quintic的坑)")
traj_overshoot = quintic(0,1,t,10,0)
print("轨迹峰值(目标只是从0到1,但可能超过1):",traj_overshoot.q.max())
print("第四部分:可视化对比")
fig, axes = plt.subplots(3, 1, figsize=(8, 8))
axes[0].plot(t, traj_q.q, label='quintic')
axes[0].plot(t, traj_t.q, label='trapezoidal')
axes[0].set_ylabel('position')
axes[0].legend()

axes[1].plot(t, traj_q.qd, label='quintic')
axes[1].plot(t, traj_t.qd, label='trapezoidal')
axes[1].set_ylabel('velocity')
axes[1].legend()

axes[2].plot(t, traj_q.qdd, label='quintic')
axes[2].plot(t, traj_t.qdd, label='trapezoidal')
axes[2].set_ylabel('acceleration')
axes[2].set_xlabel('time')
axes[2].legend()

plt.tight_layout()
plt.show()