# -*- coding: utf-8 -*-
"""
@author: foldi
"""
import matplotlib.pyplot as plt
import numpy as np

plt.close()

TFold=1
Tinga=TFold/10
omega=2*np.pi/TFold

end=1.2*TFold
time=np.linspace(0,end,1000)

theta = np.linspace(0, 2*np.pi,200)
x1 = 10*np.cos(theta)
y1 = 10*np.sin(theta)

x2 = 8*np.cos(theta)
y2 = 8*np.sin(theta)

x3 = 6*np.cos(theta)
y3 = 6*np.sin(theta)

x4 = 4*np.cos(theta)
y4 = 4*np.sin(theta)

x5 = 2*np.cos(theta)
y5 = 2*np.sin(theta)

phi=0
x0=np.linspace(-12,12,200)
x6 = np.cos(phi)*x0
y6 = np.sin(phi)*x0

phi=0.5*np.pi
x0=np.linspace(-12,12,200)
x7 = np.cos(phi)*x0
y7 = np.sin(phi)*x0

Amp=12

x0=-Amp*np.sin(2*np.pi/Tinga*time)

x8=x0*np.cos(omega*time)
y8=-x0*np.sin(omega*time)



fig, ax = plt.subplots()

ax.set_aspect('equal')

plt.plot(x1, y1, color='grey')
plt.plot(x2, y2, color='grey')
plt.plot(x3, y3, color='grey')
plt.plot(x4, y4,  color='grey')
plt.plot(x5, y5,  color='grey')

plt.plot(x6, y6,  color='grey')
plt.plot(x7, y7,  color='grey')

plt.plot(x8,y8,color='black',linewidth=3)


plt.show()





