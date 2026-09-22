"""
7.5.5 - Collision Detection 完整练习
"""

from roboticstoolbox import models
from spatialgeometry import Cuboid
from spatialmath import SE3

panda = models.URDF.Panda()
print("关节数量:",panda.n)
print("初始状态:",panda.qr)

# 场景一:箱子放在较远的位置(1.1, 0, 0),不应该碰撞
box = Cuboid([1, 1, 1], pose=SE3.Tx(1.1))
result1 = panda.iscollided(panda.qr, box)
print("\n箱子在(1.1,0,0)时,碰撞了吗?", result1)

# 场景二:把箱子挪近一点(1.0, 0, 0),应该碰撞
box.T = SE3.Tx(1)
result2 = panda.iscollided(panda.qr, box)
print("箱子在(1.0,0,0)时,碰撞了吗?", result2)

# 可视化(需要图形界面,会在浏览器打开)
env = panda.plot(panda.qr, backend="swift")
env.add(box)
env.step()