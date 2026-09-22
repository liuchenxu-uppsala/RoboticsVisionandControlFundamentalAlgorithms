"""
2.3.1.7 Unit Quaternions 练习
构造 / 组合 / 求逆 / 变换点 / ROS顺序转换
"""

import numpy as np
from spatialmath import UnitQuaternion
from spatialmath.base import rotz, rotx, roty

print("第一部分:用角度+轴,直接构造单位四元数")
# 1, 1, 1 旋转90度
axis = np.array([1,1,1])/np.sqrt(3)
theta_rad = np.deg2rad(90)
q = UnitQuaternion.AngVec(theta_rad,axis)
print("q =", q)


print("第二部分:多个旋转的组合(动坐标系,先发生写左边)")
# 场景:先绕Z转90,再绕X转45,再绕Y转65(相对每一步转完后的新坐标系)
theta_rad_1 = np.deg2rad(90)
axis_1 = np.array([0,0,1])
q1 = UnitQuaternion.AngVec(theta_rad_1,axis_1)


theta_rad_2 = np.deg2rad(45)
axis_2 = np.array([1,0,0])
q2 = UnitQuaternion.AngVec(theta_rad_2,axis_2)


theta_rad_3 = np.deg2rad(65)
axis_3 = np.array([0,1,0])
q3 = UnitQuaternion.AngVec(theta_rad_3,axis_3)
q_total = q1 * q2 * q3
print("四元数组合结果:", q_total)


# 交叉验证:矩阵连乘
R = rotz(90,unit = "deg") @ rotx(45,unit = "deg") @ roty(65,unit = "deg")
print("\n q_total == R",np.allclose(q_total.R,R))


#print("第四部分:变换一个点")
# [2, 0, 0] 这个点 在q这个新的座标系下的座标
# 交叉验证:用等价的旋转矩阵去乘同一个点
point_ = np.array([2,0,0])
posi_base_q = q_total * point_
posi_base_r = R @ point_
print("\n posi_base_q == posi_base_r",np.allclose(posi_base_r,posi_base_q))