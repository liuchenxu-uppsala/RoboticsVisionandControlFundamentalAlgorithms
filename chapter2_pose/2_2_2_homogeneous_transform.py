import numpy as np
from spatialmath.base import trot2, transl2, trplot2, plotvol2
import matplotlib.pyplot as plt

# 先平移(2,1),再旋转60度
R1 = transl2(2,1) @ trot2(60,'deg')
print("R1\n",R1)

# 先旋转60度,再平移(2,1)
R2 = trot2(60,'deg') @ transl2(2,1)
print("R2\n",R2)

print("R1 == R2 ?", np.allclose(R1, R2))

plotvol2([0, 5])
trplot2(R1, frame='A', color='b')
plt.show()