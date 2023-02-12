# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 09:58:56 2023

@author: SHREYASH
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
df=pd.read_csv("map1.txt")
p1=pd.read_csv("path1.txt")
p2=pd.read_csv("path2.txt")

P1,P2,P1_x,P1_y,P2_x,P2_y=[],[],[],[],[],[]

for i in range(20):
 P1.append(p1.iloc[i][0].split())
for i in range(20):
    P1_x.append(P1[i][0])
for i in range(20):
    P1_y.append(P1[i][1])
P1_y=[float(i) for i in P1_y]
P1_x=[float(i) for i in P1_x]

for i in range(16):
 P2.append(p2.iloc[i][0].split())
for i in range(16):
    P2_x.append(P2[i][0])
for i in range(16):
    P2_y.append(P2[i][1])
    
P2_y=[float(i) for i in P2_y]
P2_x=[float(i) for i in P2_x]




x1,x2,y1,y2=[],[],[],[]
for i in range(6):
    x1.append(df.iloc[i][0])

for i in range(6):
    y1.append(df.iloc[i][1])

for i in range(6):
    x2.append(df.iloc[i][2])

for i in range(6):
    y2.append(df.iloc[i][3])

fig=plt.figure()
ax=fig.add_subplot(111)
rect1 = matplotlib.patches.Rectangle((x1[0], y1[0]),
                                     x2[0]-x1[0], y2[0]-y1[0],
                                     color ='green')
rect2 = matplotlib.patches.Rectangle((x1[1], y1[1]),
                                     x2[1]-x1[1], y2[1]-y1[1],
                                     color ='green')  
rect3 = matplotlib.patches.Rectangle((x1[2], y1[2]),
                                     x2[2]-x1[2], y2[2]-y1[2],
                                     color ='green')
rect4 = matplotlib.patches.Rectangle((x1[3], y1[3]),
                                     x2[3]-x1[3], y2[3]-y1[3],
                                     color ='green')  
rect5 = matplotlib.patches.Rectangle((x1[4], y1[4]),
                                     x2[4]-x1[4], y2[4]-y1[4],
                                     color ='green')
rect6 = matplotlib.patches.Rectangle((x1[5], y1[5]),
                                     x2[5]-x1[5], y2[5]-y1[5],
                                     color ='green')  

plt.xlim([-5, 30])
plt.ylim([-5, 30])
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)
ax.add_patch(rect5)
ax.add_patch(rect6)
plt.plot(P1_x,P1_y)
plt.plot(P2_x,P2_y)
plt.show()
