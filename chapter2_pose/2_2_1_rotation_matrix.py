import numpy as np
from spatialmath.base import rot2, trot2, transl2, trplot2, skew, vex
from scipy import linalg

R = rot2(np.pi/4)
print("R=\n",R)

det_value = linalg.det(R)
print("\ndet:",det_value)

L = linalg.logm(R)
print("L=\n",L)

w = vex(L)
print("w =", w)
R_check = linalg.expm(L)
print("\n R_check\n",R_check)