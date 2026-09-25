"""
5.5.1 - Probabilistic Roadmap (PRM) Path Planning 练习
"""
from roboticstoolbox import PRMPlanner, rtb_load_matfile
import matplotlib.pyplot as plt

house = rtb_load_matfile("data/house.mat")
floorplan = house["floorplan"]
places = house["places"]

# ---- 用较少的点先看一下连通性差的情况 ----
prm = PRMPlanner(occgrid=floorplan, seed=0)
prm.plan(npoints=50)
print(prm)   # 观察 vertices / edges / components 数量

prm.plot()
plt.title("PRM: 50个点,连通性较差")
plt.show()

# ---- 增加点数,改善连通性 ----
prm.plan(npoints=300)
print(prm)

prm.plot()
plt.title("PRM: 300个点,连通性明显改善")
plt.show()

path1 = prm.query(start=places.br3, goal=places.kitchen)
print("路径1 (br3 -> kitchen) 途径点数:", path1.shape[0])
prm.plot(path1)
plt.title("PRM 路径: br3 -> kitchen")
plt.show()

path2 = prm.query(start=places.br2, goal=places.kitchen)
print("路径2 (br2 -> kitchen) 途径点数:", path2.shape[0])
prm.plot(path2)
plt.title("PRM 路径: br2 -> kitchen (复用同一张路网,查询很便宜)")
plt.show()