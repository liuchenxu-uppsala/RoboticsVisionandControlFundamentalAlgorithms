"""
5.4.2 - D* Path Planning 练习
对比 D* 的全量规划 vs 增量重规划(sensor 动态改变地图代价)
"""
import numpy as np
from roboticstoolbox import DstarPlanner, rtb_load_matfile
import matplotlib.pyplot as plt

