# -*- coding: utf-8 -*-
"""
@author: foldi
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

plt.close()

TFold=1
Tinga=TFold/0.1
omega=2*np.pi/TFold

end=0.25*TFold
dt=0.0005


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

time=np.linspace(0,end,1000)
Amp=12
seb_x=-12/end

x0=seb_x*time                      #gurulo test

x8=x0*np.cos(omega*time)
y8=-x0*np.sin(omega*time)

N=4
xv=np.zeros(N)

xv[2]=seb_x
idopontok = np.arange(0, end, dt)


def jobboldal (t,XV):
    a=np.zeros(2)

    vx=XV[2]
    vy=XV[3]  

    sebessegek=XV[-2:]     
    
    a[0]=2*omega*vy     #x iranyu gyorsulas, Coriolis
    a[1]=-2*omega*vx    #y iranyu gyorsulas, Coriolis
    
   
    a[0]+=XV[0]*omega*omega     #x iranyu gyorsulas, centrifugalis
    a[1]+=XV[1]*omega*omega     #y iranyu gyorsulas, centrifugalis
    
    return (np.concatenate((sebessegek,a)))

megoldas = solve_ivp(jobboldal, [0, end], xv, t_eval=idopontok)

xy=megoldas.y[:N]    

x9=xy[0]
y9=xy[1]


fig, ax = plt.subplots()

ax.set_aspect('equal')

plt.plot(x1, y1, color='grey')
plt.plot(x2, y2, color='grey')
plt.plot(x3, y3, color='grey')
plt.plot(x4, y4,  color='grey')
plt.plot(x5, y5,  color='grey')

plt.plot(x6, y6,  color='grey')
plt.plot(x7, y7,  color='grey')

plt.scatter(-12,0,color='red',linewidth=3)

plt.scatter(x8,y8,color='black',linewidth=3)

plt.plot(x9,y9,color='yellow',linewidth=3)

plt.show()





