"""
5.3 - Planning with a Graph-Based Map 完整练习
用pgraph库,构建拓扑图,分别用BFS/UCS/A*搜索路径,对比结果
"""

from pgraph import UGraph
import numpy as np
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
matplotlib.rcParams['axes.unicode_minus'] = False   # 防止负号也显示成方块
matplotlib.use('TkAgg')   # 强制用TkAgg这个后端,绕开Wayland的兼容性问题
g = UGraph()

# 加上坐标(A*需要用来算启发式距离)
g.add_vertex(name="厨房", coord=(0, 0))
g.add_vertex(name="客厅", coord=(5, 0))
g.add_vertex(name="卧室1", coord=(10, 5))
g.add_vertex(name="卧室2", coord=(10, -5))
g.add_vertex(name="浴室", coord=(15, 5))
g.add_vertex(name="大门", coord=(5, 5))

# 加上cost(代价,这里用直线距离模拟"走这条边要花多少")
g.add_edge("厨房", "客厅", cost=5)
g.add_edge("客厅", "卧室1", cost=7)
g.add_edge("客厅", "卧室2", cost=7)
g.add_edge("卧室1", "浴室", cost=5)
g.add_edge("客厅", "大门", cost=5)

print("顶点数量:", g.n)
print("边数量:", g.ne)

print("\n=== BFS ===")
path_bfs, length_bfs = g.path_BFS("卧室2", "厨房")
print("路径:", [p.name for p in path_bfs])
print("总代价:", length_bfs)

print("\n=== A* ===")
path_astar, length_astar, _ = g.path_Astar("卧室2", "厨房")
print("路径:", [p.name for p in path_astar])
print("总代价:", length_astar)

# 可视化
g.plot()
g.highlight_path(path_bfs)

import matplotlib.pyplot as plt
plt.show()   # 加上这一行,窗口才会停留、不会一闪而过