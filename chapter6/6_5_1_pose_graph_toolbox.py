"""
6.5 Pose-Graph SLAM —— 官方API demo
使用工具箱自带的PoseGraph类,加载标准g2o格式的位姿图数据,跑优化
"""
import matplotlib.pyplot as plt
from roboticstoolbox import PoseGraph
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
matplotlib.rcParams['axes.unicode_minus'] = False   # 防止负号也显示成方块
matplotlib.use('TkAgg')   # 强制用TkAgg这个后端,绕开Wayland的兼容性问题
# ---- 小规模示例(对应书里Fig 6.15/6.17,一个简单的小方块回环) ----
pg = PoseGraph("data/pg1.g2o")
print(pg)   # 打印顶点数、边数

plt.figure()
pg.plot()
plt.title("优化前: 顶点位置因累积误差而扭曲")
plt.savefig("posegraph_before.png", dpi=150)

# 跑优化, animate=True会展示顶点逐步"松弛"到更合理位置的动画
pg.optimize(animate=True)
# 会打印每一轮的总代价(总误差), 应该逐渐逼近0, 比如:
#   done in 4.60 msec. Total cost 316.88
#   done in 2.66 msec. Total cost 47.2186
#   ...
#   done in 2.09 msec. Total cost 3.14139e-11

plt.figure()
pg.plot()
plt.title("优化后: 顶点收敛到自洽配置")
plt.savefig("posegraph_after.png", dpi=150)
plt.show()

# ---- 大规模真实数据(MIT Killian Court, 1941个顶点/3995条边) ----
pg_big = PoseGraph("data/killian-small.toro")
print(pg_big)

plt.figure()
pg_big.plot()
plt.title("大规模位姿图优化前: 两趟走廊严重错位")
plt.savefig("killian_before.png", dpi=150)

pg_big.optimize()

plt.figure()
pg_big.plot()
plt.title("大规模位姿图优化后: 两趟走廊基本重合")
plt.savefig("killian_after.png", dpi=150)
plt.show()