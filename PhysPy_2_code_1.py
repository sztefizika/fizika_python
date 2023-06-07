# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import time

start=time.time()


dt=0.01
D=1.0
m=1.0
g=10.0
gamma=0.1
mu=0#0.002
steps=0

t=0.0    
x=1.0
v=0.0

tlist=[t]
xlist=[x]
vlist=[v]
Elist=[0.5*m*v*v+0.5*D*x*x]


def F(x,v,t):
    return -D*x-gamma*v-np.copysign(1,v)*m*g*mu

while t<120.0:
    kx1=v*dt
    kv1=F(x,v,t)/m*dt
    
    kx2=(v+0.5*kv1)
    kv2=F(x+0.5*kx1,v+0.5*kv1,t+0.5*dt)/m
    
    x+=kx2*dt
    v+=kv2*dt
    t+=dt
    
    steps+=1
    
    if  steps%20==0:
        tlist.append(t)
        xlist.append(x)
        vlist.append(v)
        Elist.append(0.5*m*v*v+0.5*D*x*x)
        #print(0.5*m*v*v+0.5*D*x*x)
    

#conda install -c conda-forge ffmpeg

#https://matplotlib.org/2.0.2/examples/animation/moviewriter.html

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='damped oscillator', artist='none',
                comment='two dots representing interacting oscillators')
writer = FFMpegWriter(fps=30, metadata=metadata)

# Initialize the movie
fig = plt.figure()

zero_line1, = plt.plot([0,0], [-4,210], 'black')
x1_line, =plt.plot(xlist,tlist)
red_circle, = plt.plot([], [], 'ro', markersize = 10)
plt.xlabel('x')
plt.ylabel('t')
plt.axis([-1.1, 1.1, -3.2, 3.2])

# Update the frames for the movie
with writer.saving(fig, "osc.mp4", 100):
    for i in range(600):
        plt.axis([-1.1, 1.1, -3.2+i*20*dt, 3.2+i*20*dt])
        X = xlist[i]
        y0 = i*dt*20
        red_circle.set_data(X, y0)
        writer.grab_frame()

stop=time.time()

print("Futásidő:", '%.3f' % (stop-start), " s")
