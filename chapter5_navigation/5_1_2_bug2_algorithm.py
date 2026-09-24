from roboticstoolbox import Bug2, rtb_load_matfile
import matplotlib.pyplot as plt

house = rtb_load_matfile("data/house.mat")
floorplan = house["floorplan"]
places = house["places"]

bug = Bug2(occgrid=floorplan)
bug.plot()

path = bug.run(start=places.br3, goal=places.kitchen)
print("路径总共多少步:", path.shape[0])

plt.figure()
plt.imshow(floorplan, cmap='gray_r', origin='lower')
plt.plot(path[:,0], path[:,1], 'r.-', markersize=2)
plt.show()