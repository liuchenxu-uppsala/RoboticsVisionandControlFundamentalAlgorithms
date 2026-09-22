import numpy as np
from spatialmath.base import skew
from scipy.linalg import expm

# --- 1. 线速度计算 ---
# 角速度 1.0, 2.0, 2.0
# 位置 1.0, 0.0, 0.0
w = np.array([1.0,2.0,2.0])
position  = np.array([1.0,0.0,0.0])
velocity = skew(w) @ position
print("\n线速度 velocity: ",velocity)



# --- 2. 指数映射计算旋转矩阵 ---
# 旋转轴 0.0, 1.0, 1.0 
# 旋转角度 60
n = np.array([0.0,1.0,1.0])
n_unit = n/np.linalg.norm(n)
angle_rad = np.deg2rad(60)
R = expm(angle_rad * skew(n_unit))
print("\n旋转矩阵 R:\n", R)