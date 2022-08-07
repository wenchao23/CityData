import shapefile
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import obstacle_gen
from open3d import *    
import open3d as o3d
myshp = open("mga55/mga55.shp", "rb")
mydbf = open("mga55/mga55.dbf", "rb")
sf = shapefile.Reader(shp=myshp, dbf=mydbf)

shapes = sf.shapeRecords()
listx = []
listy = []
listz = []
listxx = []
listyy = []
listzz = []

i = 1
j = 1

fig = plt.figure()
ax = Axes3D(fig)

for shape in shapes:
    h = shape.record[1]
    if h >100:

        for x, y in  shape.shape.points:
            listx.append(x)
            listy.append(y)
            listz.append(0)
        temp = np.array([np.min(listx),np.min(listy),0,np.max(listx)-np.min(listx),np.max(listy)-np.min(listy), h])
        if j ==1:
            points = temp
        else: 
            points = np.concatenate((points,temp), axis = 0)
     
        for i in np.arange(start = 0, stop = listx.__len__() - 1, step = 1):
            listxx.append(listx[i])
            listyy.append(listy[i])
            listzz.append(0)
            listxx.append(listx[i])
            listyy.append(listy[i])   
            listzz.append(h)   
            listxx.append(listx[i+1])
            listyy.append(listy[i+1])   
            listzz.append(h)   
            listxx.append(listx[i+1])
            listyy.append(listy[i+1])   
            listzz.append(0)
            listxx.append(listx[i])
            listyy.append(listy[i])   
            listzz.append(0)

            verts1 = [list(zip(listxx,listyy,listzz))]
            listxx = []
            listyy = []
            listzz = []

        listx=[]
        listy=[]
        listz=[]
        j = j+1



row = int(points.__len__()/6)
points = np.reshape(points,(row,6))
for i in np.arange(start = 0, stop =row, step = 1):    
    poistion = [points[i,0:3].tolist()]
    size = [points[i,-3:].tolist()]
    obstacle_gen.plotCubeAt2(ax,poistion,size,color = 'darkgrey', linewidths=1)
    # print(poistion)

    # pcd = o3d.io.read_point_cloud("input.txt", format="xyz")
    # o3d.io.write_point_cloud("output.ply", poistion)

ax.set_xlim((318000, 322000))
ax.set_ylim((5811000, 5815000))
ax.set_zlim((0, 150))
plt.savefig('demo.png')
plt.show()