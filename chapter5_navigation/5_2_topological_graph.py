from pgraph import UGraph

g = UGraph()

g.add_vertex(name="厨房")
g.add_vertex(name="客厅")
g.add_vertex(name="卧室1")
g.add_vertex(name="卧室2")
g.add_vertex(name="浴室")
g.add_vertex(name="大门")

# 每条边,补上cost参数(可以用距离,或者随便设一个1,表示"走一步"的代价)
g.add_edge("厨房", "客厅", cost=1)
g.add_edge("客厅", "卧室1", cost=1)
g.add_edge("客厅", "卧室2", cost=1)
g.add_edge("卧室1", "浴室", cost=1)
g.add_edge("客厅", "大门", cost=1)

print("顶点数量:", g.n)
print("边数量:", g.ne)

path = g.path_Astar("卧室2", "厨房")
print("\n从卧室2到厨房的路径:", path)