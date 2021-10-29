import numpy as np
import pylab
import matplotlib.pyplot as plt
import math
import scipy.ndimage as ndimage

fig = plt.figure(figsize=(6, 6))



ax1 = fig.add_subplot(2,2,1)
x = [2, 2, 4, 5, 6, 8, 8, 2]
y = [1, 6, 3, 6, 3, 6, 1, 1]


ax1.plot(x, y,
            color = 'blue')
plt.title(" Вариант №8 ")
pylab.xlim (-10, 20)
pylab.ylim (-10, 20)

ax1.hlines(0, -10, 20,linestyle = '--' )
ax1.vlines(0, -10, 20,linestyle = '--' )


print("""Укажите какое преобразование хотите выполнить:
1 - Параллельный перенос
3 - Симметрия относительно оси oY
4 - Симметрия относительно оси oX
5 - Масштабирование
6 - Выход""")
choice = int(input())
if choice == 1:
        q = int(input("На сколько единиц осуществить перенос: "))
        ax2 = fig.add_subplot(2,2,2)
        x1 = [2, 2, 4, 5, 6, 8, 8, 2]
        y1= [1, 6, 3, 6, 3, 6, 1, 1]
        x2 = []
        y2 = []
        
        for i in x1:
            i += q
            x2.append(i)
        for i in y1:
            i += q
            y2.append(i)
        ax2.plot(x2, y2,
            color = 'blue')
        plt.title(" Перенос ")
        pylab.xlim (-10, 20)
        pylab.ylim (-10, 20)

        ax2.hlines(0, -10, 20,linestyle = '--' )
        ax2.vlines(0, -10, 20,linestyle = '--' )

        
        
elif choice == 5:
        a = int(input("Введите во сколько раз хотите масштабировать фигуру: "))
        if a>4:
            print("Не влезет в систему координат")
            exit()
        else:
            ax2 = fig.add_subplot(2,2,2)
            x1 = [2, 2, 4, 5, 6, 8, 8, 2]
            y1= [1, 6, 3, 6, 3, 6, 1, 1]
            x2 = []
            y2 = []
            
            for i in x1:
                i *= a
                x2.append(i)
            for i in y1:
                i *= a
                y2.append(i)
            ax2.plot(x2, y2,
                color = 'blue')
            
            plt.title(" Масштабирование ")
            pylab.xlim (-10, 20)
            pylab.ylim (-10, 20)

            ax2.hlines(0, -10, 20,linestyle = '--' )
            ax2.vlines(0, -10, 20,linestyle = '--' )
            
elif choice == 3:
        ax2 = fig.add_subplot(2,2,2)
        x1 = [2, 2, 4, 5, 6, 8, 8, 2]
        y1= [1, 6, 3, 6, 3, 6, 1, 1]

        y2 = []
        
        for i in y1:
            i *= -1
            y2.append(i)
            
        ax2.plot(x1, y2,
            color = 'blue')
        plt.title(" Симметрия по оси")
        pylab.xlim (-10, 20)
        pylab.ylim (-10, 20)

        ax2.hlines(0, -10, 20,linestyle = '--' )
        ax2.vlines(0, -10, 20,linestyle = '--' )

elif choice == 4:
        ax2 = fig.add_subplot(2,2,2)
        x1 = [2, 2, 4, 5, 6, 8, 8, 2]
        y1= [1, 6, 3, 6, 3, 6, 1, 1]

        x2 = []
        
        for i in x1:
            i *= -1
            x2.append(i)
            
        ax2.plot(x2, y1,
            color = 'blue')
        plt.title(" Симметрия по оси OY ")
        pylab.xlim (-10, 20)
        pylab.ylim (-10, 20)

        ax2.hlines(0, -10, 20,linestyle = '--' )
        ax2.vlines(0, -10, 20,linestyle = '--' )

elif choice==6:
        exit()
plt.show()
    

