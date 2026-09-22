"""
Chapter 7 - 7.1.1.1 Forward Kinematics from a Pose Graph (2D)
用ETS(Elementary Transformation Sequence)构建2D机械臂运动学链
"""

import numpy as np
from roboticstoolbox import ET2

# print("第一部分:单关节机械臂(钟表指针)")
a1 = 1
e1 = ET2.R() * ET2.tx(a1)
print("链条结构:", e1)
print("关节数量:", e1.n)
# 代入具体角度,求FK pi/4
e1.fkine(np.pi/4)
# 交互式可视化(会弹出GUI,需要图形界面支持)
#e1.teach(np.array([np.pi/4]))

print(15 * "===")

# print("第二部分:两关节机械臂")
# 角度 分别是 20, 30 连杆长度都是1
a1,a2 = 1,1
e2 = ET2.R() * ET2.tx(a1) * ET2.R() * ET2.tx(a2)
print("e2[0] (第1段,应该是关节R):", e2[0])
print("e2[1] (第2段,应该是连杆tx):", e2[1])
print("e2[1].eta (这段的常数参数):", e2[1].eta)
print("e2[1].A() (这段单独的变换矩阵):\n", e2[1].A())
T2 = e2.fkine(np.deg2rad([20,30]))
print("q0=20度, q1=30度时的末端位姿:\n", T2)
#e2.plot(np.deg2rad([20, 30]))
e2.teach(np.deg2rad([20, 30]))

'''

T1 = e1.fkine(np.pi / 4) 得到的是旋转矩阵是吧？
2、哪种才会让让e2.structure 输出P的那种类型的关节呢？我看我们的例子中都没有过P的类型的关节是吧？
'''
