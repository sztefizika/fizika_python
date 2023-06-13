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
mu=0.0
steps=0;

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
        print(0.5*m*v*v+0.5*D*x*x)
    
    
#plt.plot(xlist, vlist)
#plt.plot(tlist, Elist)

#conda install -c conda-forge ffmpeg

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='damped oscillator -- phase space', artist='none',
                comment='two dots representing interacting oscillators')
writer = FFMpegWriter(fps=30, metadata=metadata)

# Initialize the movie
fig = plt.figure()

zero_line1, = plt.plot([0,0], [-2,2], 'black')
zero_line2, = plt.plot([-2,2], [0,0], 'black')
x1_line, =plt.plot(xlist,vlist,"lightgrey")
blue_spiral, = plt.plot([], [])
red_circle, = plt.plot([], [], 'ro', markersize = 10)
plt.xlabel('x')
plt.ylabel('p')
plt.axis([-1.1, 1.1, -1.1, 1.1])

# Update the frames for the movie
with writer.saving(fig, "fazister.mp4", 100):
    for i in range(600):
        #plt.axis([-1.1, 1.1, -3.2+i*20*dt, 3.2+i*20*dt])
        X = xlist[i]
        V= vlist[i]
        red_circle.set_data(X, V)
        blue_spiral.set_data(xlist[:i],vlist[:i])
        writer.grab_frame()

stop=time.time()

print("Futásidő:", '%.3f' % (stop-start), " s")
