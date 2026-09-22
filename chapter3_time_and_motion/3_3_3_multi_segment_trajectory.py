import numpy as np
from roboticstoolbox import mstraj
import matplotlib.pyplot as plt

via = np.array([[0,0,0.1],[0,0,0],[1,0,0],[1,1,0],[1,1,0.1]])

traj = mstraj(via,qdmax=[0.5, 0.5, 0.5],q0=via[0],dt=0.02, tacc=0.2)

print("经过多少个点:",traj.q.shape[0])

print("每个点有几个维度(应该是3, 对应xyz):", traj.q.shape[1])

print("\n起点:", traj.q[0])
print("终点:", traj.q[-1])

# 画出XY平面的路径,看看轨迹怎么"抄近路"绕过中间点
plt.figure()
plt.plot(traj.q[:, 0], traj.q[:, 1], 'b-', label='Real')
plt.plot(via[:, 0], via[:, 1], 'ro--', label='Via')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('mstraj: real vs expected')
plt.show()
