"""
7.2.2.1 - PUMA 560 解析解IK,完整验证流程
"""

from roboticstoolbox import models
from spatialmath import SE3

# 第一步:用一组已知的关节角度(标准姿态qn),算FK,得到目标位姿T
puma560 = models.DH.Puma560()
init_angles = puma560.qn
T = puma560.fkine(init_angles)
# 第二步:把T当作目标,反过来求解IK(解析解)
sol = puma560.ikine_a(T)
print("\nIK求解成功吗?", sol.success)
print("求出的关节角度:", sol.q)

# 第三步:验证——把求出来的角度,重新代入FK,应该得到同一个T
T2 = puma560.fkine(init_angles)
print("T == T2",T == T2)
# 第四步:尝试一个超出可达范围的目标,观察"无解"的情况
sol_fail = puma560.ikine_a(SE3.Tx(3))
print("\n超出范围的目标,求解结果:")
print("成功吗?", sol_fail.success)
print("失败原因:", sol_fail.reason)
