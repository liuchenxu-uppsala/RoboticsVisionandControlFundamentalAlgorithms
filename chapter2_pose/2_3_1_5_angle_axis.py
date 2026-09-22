"""
2.3.1.5 Rotation About an Arbitrary Vector 练习
从旋转矩阵,反解出"角度+轴"这种表示;并验证能还原回去
"""

import numpy as np
from spatialmath.base import rpy2r, tr2angvec, angvec2r

# 用一个已知的RPY姿态,构造旋转矩阵 "zyx"  0.1, 0.2, 0.3
R = rpy2r(0.1,0.2,0.3,order="zyx")
print("\nR:",R)
# 反解出角度和轴
theta, v = tr2angvec(R)
print("旋转角度 theta =", theta)
print("旋转轴 v =", v)
# 反过来验证:用角度+轴,还原回旋转矩阵
R_check = angvec2r(theta,v)
print("从角度和轴 还原出来的旋转矩阵 与 计算出来的R 是否相等",np.allclose(R_check,R))
