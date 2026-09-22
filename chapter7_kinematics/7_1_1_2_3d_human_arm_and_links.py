"""
7.1.1.2 - 3D机械臂(6自由度人形手臂结构)
7.1.2 - 以连杆为中心的建模方式(Link2)
"""


import numpy as np
from roboticstoolbox import ET, ET2, Link2


print("=" * 50)
print("第一部分:6自由度人形手臂(3D ET)")
print("=" * 50)

a1,a2 = 1,1
e = (ET.Rz() * ET.Ry()           # 肩:2自由度
     * ET.tz(a1) * ET.Ry()        # 上臂 + 肘
     * ET.tz(a2)                   # 下臂
     * ET.Rz() * ET.Ry() * ET.Rz())  # 腕:3自由度(ZYZ)

# "关节数量" "关节类型简写"
print("关节数量:",e.n)
print("关节类型简写",e.structure)
# 全零姿态,求FK
rads = np.zeros(6)
R = e.fkine(rads)
print("R:",R)
# 换一组具体角度,求FK 10, 20, 30, 15, 25, 5
rads = np.deg2rad([10, 20, 30, 15, 25, 5])
R = e.fkine(rads)
print("R:",R)
# 交互可视化
e.teach(rads)


print()
print("=" * 50)
print("第二部分:以连杆为中心的建模(Link2,2D例子)")
print("=" * 50)


# a1 = 1 a2 = 1
link1 = Link2(ET2.R(),name = "link1")
link2 = Link2(ET2.tx(1)*ET2.R(),name = "link2",parent=link1 )
link3 = Link2(ET2.tx(1),name = "link3",parent=link2)
print(link1)
print("link2: ",link2,"的父节点是",link2.parent.name)
print("link3: ",link3,"的父节点是",link3.parent.name)