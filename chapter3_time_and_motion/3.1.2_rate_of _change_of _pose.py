"""
3.1.2 - Rate of Change of Pose,完整演示
从随时间变化的位姿T(t),数值求导,算出6维空间速度 nu = (v, omega)
"""

import numpy as np
from spatialmath.base import rotz, vex

'''
定义函数 返回对应的齐次矩阵
旋转 2 * t 然后沿着X轴平移 速度是1 
'''
def T(t):
    qt = np.eye(4)
    qt[:3,:3] = rotz(2* t)
    qt[:3,3] = rotz(2* t) @ np.array([t,0,0])
    return qt

# t = 0.5
t = 0.5
dt = 1e-6
dot_R = ( T(t+dt) - T(t) ) / dt
v = dot_R[:3,3]
print("线速度:",v)

R = T(t)[:3,:3]
R_dot = dot_R[:3,:3]
w = R_dot @ R.T
rw = vex(w)
print("角速度:",rw)
