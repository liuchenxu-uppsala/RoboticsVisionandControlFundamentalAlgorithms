import numpy as np
from spatialmath.base import rotx, roty, rotz, eul2r, tr2eul, rpy2r, tr2rpy

# 手动拼三段旋转(ZYZ顺序) 0.1, 0.2, 0.3
R_old = rotz(0.1) @ roty(0.2) @ rotz(0.3)
# 用eul2r一步到位(默认就是ZYZ顺序)
R_new = eul2r(0.1,0.2,0.3)
#print("两者一致吗?", np.allclose(R_manual, R_eul))
print("1两者一致吗?", np.allclose(R_old, R_new))

# 反解:从旋转矩阵,还原出ZYZ角度
eul_angle = tr2eul(R_new)
print("\neul_angle:\n",eul_angle)
# roll, pitch, yaw ZYX顺序(交通工具姿态) 0.1, 0.2, 0.3

# 手动拼接:R = Rz(yaw) @ Ry(pitch) @ Rx(roll)
R_old = rotz(0.1) @ roty(0.2) @ rotx(0.3)
# 用rpy2r一步到位,注意参数顺序是 roll, pitch, yaw zyx顺序
R_new = rpy2r(0.3,0.2,0.1,order = "zyx")
# 两者一致吗
print("2两者一致吗?", np.allclose(R_old, R_new))
# 反解
print("\n rpy反解 \n",tr2rpy(R_new,order= "zyx"))

# # 手动拼接 xyz  顺序 0.1, 0.2, 0.3 
R_old = rotx(0.3) @ roty(0.2) @ rotz(0.2)
# rpy2r 做一遍 注意顺序
R_new = rpy2r(0.2,0.2,0.3,order = "xyz")
print("3两者一致吗?", np.allclose(R_old, R_new))
#反解角度
print("3 rpy反解 \n",tr2rpy(R_new,order= "xyz"))

print(15 * "==")
R_old = rotz(0.1) @ roty(0.2) @ rotx(0.3)
R_new = rpy2r(0.3,0.2,0.1,order = "zyx") 
print("4两者一致吗?", np.allclose(R_old, R_new))