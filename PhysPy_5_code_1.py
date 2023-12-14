# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.integrate import solve_ivp
#import matplotlib.animation as manimation


start=time.time()


N=1000
dt=2
D=1.0
m=1.0
T=1500.0
x0=500

xv=np.zeros(2*N)
melyikpont=np.arange(2*N)

xv=np.exp(-(melyikpont-x0)*(melyikpont-x0)/10)

melyikpont=np.arange(N)


idopontok = np.arange(0, T, dt)

def jobboldal (t,XV):
    a=np.zeros(N)

    x=XV[:N]    
    v=XV[-N:]
  
    a=np.zeros(N)

    for i in range(1, N-1) :
        a[i]=D*(x[i-1]+x[i+1]-2*x[i])/m;
    
    a[0]=0     #rögzített vég
    a[N-1]=0   #rögzített vég
    
    #a[0]=D*(x[1]-x[0])/m        #szabad vég
    #a[N-1]=D*(x[N-2]-x[N-1])/m  #szabad vég
   
    
    #a[0]=D*(x[N-1]+x[1]-2*x[0])/m      #periodikus
    #a[N-1]=D*(x[N-2]+x[0]-2*x[N-1])/m  #periodikus
    
    
    return (np.concatenate((v,a)))

megoldas = solve_ivp(jobboldal, [0, T], xv, t_eval=idopontok)

x=megoldas.y[:N]    
v=megoldas.y[-N:]


Time,Pont=np.meshgrid(megoldas.t,melyikpont)
axes=plt.axes(projection ='3d')
axes.plot_surface(Time,Pont, x, cmap="autumn") 

plt.show    


"""

#itt készül a videó
#Ezt a jó a rögzített és a szabad véghez
toplot=np.zeros(N)

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='wave along a line', artist='none',
                comment='The ends are fixed')
writer = FFMpegWriter(fps=30, metadata=metadata)

# Initialize the movie
fig = plt.figure()

plt.xlabel('pozíció')
plt.ylabel('kitérés')

plt.ylim(-0.5,1.2)

# Update the frames for the movie
with writer.saving(fig, "wave.mp4", 100):
    for k in range(700):
        
        plt.plot(melyikpont,toplot,color='white',linewidth=10)
        for i in range(0, N) :
            toplot[i]=x[i][k]
        plt.plot(melyikpont,toplot,color='red',linewidth=1)
        
        writer.grab_frame()
"""

"""

#itt készül a videó
#Ezt a jó a periodikus peremfeltételhez

toplot=np.zeros(N)
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='wave along a circle', artist='none',
                comment='periodic boundary condition')
writer = FFMpegWriter(fps=30, metadata=metadata)

# Initialize the movie
fig = plt.figure()
axes=plt.axes(projection ='3d')
axes.set_zlim(-0.2,1)

for i in range(0, N) :
    toplot[i]=x[i][0]
    
axes.plot(np.cos(2*np.pi*melyikpont[:N]/N), np.sin(2*np.pi*melyikpont[:N]/N),toplot)

# Update the frames for the movie
with writer.saving(fig, "wave.mp4", 100):
    for k in range(750):
        
        #axes.plot(np.cos(2*np.pi*melyikpont[:N]/N), np.sin(2*np.pi*melyikpont[:N]/N),toplot,color='white',linewidth=2)
        for i in range(0, N) :
            toplot[i]=x[i][k]
        axes.plot(np.cos(2*np.pi*melyikpont[:N]/N), np.sin(2*np.pi*melyikpont[:N]/N),toplot,color='red',linewidth=1)
        
        writer.grab_frame()
"""

stop=time.time()

print("Futásidő:", '%.3f' % (stop-start), " s")
