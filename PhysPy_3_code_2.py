# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.time()


dt=0.01
D=1.0
m=1.0
g=10.0
gamma=0.1#0.1
mu=0.0#0.002
steps=0

F0=0.4
omega=0.4

t=0.0    
x=1.0
v=0.0

tlist=[t]
xlist=[x]
vlist=[v]
Elist=[0.5*m*v*v+0.5*D*x*x]


def F(x,v,t):
    return -D*x-gamma*v-F0*np.sin(omega*t)

while t<200.0:
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
    
#vlist=np.cos(tlist)
    
plt.plot(xlist,vlist)
#plt.plot(tlist, Elist)


stop=time.time()

print("Futásidő:", '%.3f' % (stop-start), " s")
