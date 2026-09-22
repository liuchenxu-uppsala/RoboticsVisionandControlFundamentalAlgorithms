"""
7.1.4 - URDF: 读取和使用机器人模型文件
"""

from roboticstoolbox import models

# 加载库自带的UR5机械臂(经典协作机械臂,URDF模型内置)
ur5 = models.URDF.UR5()
print("机器人名称、关节数、结构信息:")
print(ur5)
print("\n夹爪信息:")
print(ur5.grippers)
# 查看结构图(会画出树状结构,能看到"分支")
#ur5.showgraph()
# 用模型自带的预设姿态,渲染3D模型(会在浏览器打开一个新标签页)
ur5.teach(ur5.qr, backend='swift')
input("按回车键退出...")