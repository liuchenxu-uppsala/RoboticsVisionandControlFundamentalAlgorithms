"""
3.3.4 - Interpolation of Orientation in 3D 练习
对比 RPY插值 vs 四元数SLERP插值
"""

import numpy as np
from spatialmath import SO3, UnitQuaternion
from roboticstoolbox import mtraj, quintic

# 开始 z 转 -1,y 转 -1
start = SO3.Rz(-1) * SO3.Ry(-1)
end = SO3.Rz(1) * SO3.Ry(1)
# 结束 z 转 1 y 转 1

print("方法一:RPY插值")

rpy0 = start.rpy()
rpy1 = end.rpy()


print("起点RPY:", rpy0)
print("终点RPY:", rpy1)


traj_rpy = mtraj(quintic,rpy0,rpy1,50)
pose_from_rpy = SO3.RPY(traj_rpy.q)
print("方法二:四元数SLERP插值")
q0 = UnitQuaternion(start)
q1 = UnitQuaternion(end)
qtraj = q0.interp(q1, 50)
qtraj.animate()
print("插值出的中间姿态数量:", len(qtraj))

# 对比中间某一点(比如第25步),两种方法算出的姿态是否一致
mid_R_from_rpy = pose_from_rpy[25].R
mid_R_from_slerp = qtraj[25].R
print("\n中间点姿态一致吗?", np.allclose(mid_R_from_rpy, mid_R_from_slerp, atol=0.05))