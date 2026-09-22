import numpy as np
from spatialmath.base import transl2, trot2

# ^A T_B:{B}相对{A},平移了(2,1),旋转了30度
R = transl2(2,1) @ trot2(30,'deg')
print("R:\n",R)

# 一个点,在{B}坐标系下的坐标是 (5, 6)
poit_B = np.array([5,6,1])
point_A = R @ poit_B
print("point_A:\n",point_A)

# 反过来验证:从A系,求回B系下的坐标
point_test = np.linalg.inv(R) @ point_A
print("point_test:\n",point_test)

eq  = np.allclose(point_test,poit_B)
print("poit_B = point_test",eq)