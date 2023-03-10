import matplotlib.pyplot as plt
import numpy as np
dx = 0.01, dy = 0.01
x = np.arange(-2.5,2.5,dx)
y = np.arange(-2.5,3.5,dy)
X,Y = np.meshgrid(x,y)
def f(x,y):
    return (1 - y**5 + x**5)*np.exp(-x**2-y**2)
C = plt.contourf(X,Y,f(x,y),8,colors='black')
plt.contourf(X,Y,f(x,y),8,cmap=plt.cm.hot)
plt.clabel(C, inline=1, fontsize=10)
plt.colorbar()
plt.show()
