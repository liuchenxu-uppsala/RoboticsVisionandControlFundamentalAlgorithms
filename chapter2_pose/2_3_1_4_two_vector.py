import numpy as np
from spatialmath.base import oa2r

# 场景:夹爪朝下(接近向量 Z轴 指向 -Z),手指连线沿(1,1,0)方向
o = [1,1,0]
a = [0,0,-1]
R = oa2r(o,a)
# 验证正交性(我们反复讲过的旋转矩阵性质)
n = np.cross(o / np.linalg.norm(o),a)
print("0 第一个旋转矩阵",R)
print("\n 1 叉乘出来的结果:",n)
print("\n 2 旋转矩阵的第一列:",R[:,0])
print("\n 3 行列式值:",np.linalg.det(R))
# 验证:第三列(法向量n)确实是 o 叉乘 a 算出来的

# 换一个场景:夹爪水平伸出(从侧面抓),手指连线沿竖直方向
o = [0,0,1]
a = [1,0,0]
R = oa2r(o,a)
print("新场景的旋转矩阵",R)