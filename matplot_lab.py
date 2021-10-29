import numpy as np
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import *

fig = plt.figure(figsize=(10, 6))
ax_3d = fig.add_subplot(2,2,4, projection = '3d')

#Основание усеченной пирамиды O1

x1 = [4,10]
y1 = [1,1]
z1 = [1,1]

x2 = [4,4]
y2 = [1,7]
z2 = [1,1]

x3 = [4,10]
y3 = [7,7]
z3 = [1,1]

x4 = [10,10]
y4 = [1,7]
z4 = [1,1]

#Основание усеченной пирамиды O2

x5 = [5,9]
y5 = [2,2]
z5 = [6,6]

x6 = [5,5]
y6 = [2,6]
z6 = [6,6]

x7 = [5,9]
y7 = [6,6]
z7 = [6,6]

x8 = [9,9]
y8 = [2,6]
z8 = [6,6]

#Грани

x9 = [4,5]
y9 = [1,2]
z9 = [1,6]

x10 = [4,5]
y10 = [7,6]
z10 = [1,6]

x11 = [10,9]
y11 = [7,6]
z11 = [1,6]

x12 = [10,9]
y12 = [1,2]
z12 = [1,6]

#Построение

ax_3d.plot(x1, y1, z1, color = 'blue')
ax_3d.plot(x2, y2, z2, color = 'blue')
ax_3d.plot(x3, y3, z3, color = 'blue')
ax_3d.plot(x4, y4, z4, color = 'blue')

ax_3d.plot(x5, y5, z5, color = 'blue')
ax_3d.plot(x6, y6, z6, color = 'blue')
ax_3d.plot(x7, y7, z7, color = 'blue')
ax_3d.plot(x8, y8, z8, color = 'blue')

ax_3d.plot(x9, y9, z9, color = 'blue')
ax_3d.plot(x10, y10, z10, color = 'blue')
ax_3d.plot(x11, y11, z11, color = 'blue')
ax_3d.plot(x12, y12, z12, color = 'blue')

#Проекции

#Горизонтальная

ax = fig.add_subplot(2,2,1)

x = [4, 4, 10, 10 ,4]
y = [1, 7, 7, 1, 1]

x1 = [5, 5, 9, 9, 5]
y1 = [2, 6, 6, 2, 2]

ax.plot(x, y,
        color = 'black')

ax.plot(x1, y1,
        color = 'black')

plt.title("Горизонтальная проекция")
pylab.xlim (0, 12)
pylab.ylim (0, 8)

#Фронтальная
ax1 = fig.add_subplot(2,2,2)
x = [4, 5, 9, 10,4]
y = [1, 6, 6, 1, 1]


ax1.plot(x, y,
        color = 'blue')
plt.title(" Фронтальная проекция")
pylab.xlim (0, 12)
pylab.ylim (0, 8)

#Профильная
ax2 = fig.add_subplot(2,2,3)
x = [1, 2, 6, 7, 1]
y = [1, 6, 6, 1, 1]


ax2.plot(x, y,
        color = 'blue')
plt.title(" Профильная проекция")
pylab.xlim (0, 12)
pylab.ylim (0, 8)

plt.show()
