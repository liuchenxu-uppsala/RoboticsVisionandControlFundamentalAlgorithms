import numpy as np
from spatialmath import Twist2
from spatialmath.base import transl2, trot2

# 目标:绕点 C=(3,2),旋转45度
C = np.array([3, 2])
R_old = transl2(C) @ trot2(45,'deg') @ transl2(-C)
print("R_old:\n",R_old)

rad = np.deg2rad(45)
S = Twist2.UnitRevolute(C)
R_new = S.exp(rad)
print("R_old == R_new",np.allclose(R_old,R_new))


# 目标:沿方向(1,1)(需要单位化),平移距离为3
direction = np.array([1,1])/np.sqrt(2)
R_old = transl2(3*direction,3*direction)
S = Twist2.UnitPrismatic(direction)
R_new = S.exp(3)
print("R_old == R_new",np.allclose(R_old,R_new))