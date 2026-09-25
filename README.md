# Robotics, Vision and Control - 学习笔记与代码练习

跟随 Peter Corke 《Robotics, Vision and Control: Fundamental Algorithms in Python》(第三版)一书,进行的学习练习代码,配合 WARA Robotics Challenge 项目的准备工作。

## 复习笔记

- [第2章复习:Representing Position and Orientation](./chapter2_pose/chapter2_review.md)
- [第3章复习:Time and Motion](./chapter3_time_and_motion/chapter3_review.md)
- [第4章复习:Mobile Robot Vehicles](./chapter4_mobile_robots/chapter4_review.md)
- [第5章复习:Navigation](./chapter5_navigation/chapter5_review.md)
- [第7章复习:Robot Arm Kinematics](./chapter7_kinematics/chapter7_review.md)

（后续章节继续在这里追加链接）

## 目录结构

- `chapter2_pose/` — 第2章:位置与姿态表示(坐标变换、旋转矩阵、四元数、旋量等)
- `chapter3_time_and_motion/` — 第3章:时间与运动(位姿的导数、空间速度、轨迹生成quintic/trapezoidal/mstraj、姿态插值)
- `chapter4_mobile_robots/` — 第4章:移动机器人车辆(汽车/自行车模型、差速驱动/独轮车模型、全向轮/麦克纳姆轮)
- `chapter5_navigation/` — 第5章:导航(反应式导航/Bug2、图搜索BFS-UCS-A\*、占据栅格规划Distance Transform/D\*、概率路图PRM、可行驶路径规划Dubins/Reeds-Shepp/Lattice/RRT)
- `chapter7_kinematics/` — 第7章:机械臂运动学(D-H参数、正/逆运动学、轨迹生成、碰撞检测等)

## 环境

- Python 3.12
- ROS 2 Jazzy Jalisco
- roboticstoolbox-python
- spatialmath-python
