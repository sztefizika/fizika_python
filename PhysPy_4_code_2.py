# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


dt=0.01
Dx=4.0
Dy=1.0 #korfrekvencia=sqrt(D/m)
m=1.0

t=0.0    
x=1.0
vx=5.0
y=1.0
vy=0.0

tlist=[t]
xlist=[x]
vxlist=[vx]
ylist=[y]
vylist=[vy]
Elist=[0.5*m*vx*vx+0.5*Dx*x*x+0.5*m*vy*vy+0.5*Dy*y*y]

def Fx(x,vx,t):
    return -Dx*x

def Fy(x,y,vx,vy,t):
    return -Dy*y

while t<10.0:
    print(vx)
    kx1=vx*dt
    kvx1=Fx(x,vx,t)/m*dt
    kx2=(vx+0.5*kvx1)
    
    ky1=vy*dt
    kvy1=Fy(x,y,vx,vy,t)/m*dt
    ky2=(vy+0.5*kvy1)
    
    kvx2=Fx(x+0.5*kx1,vx+0.5*kvx1,t+0.5*dt)/m
    kvy2=Fy(x+0.5*kx1,y+0.5*ky1,vx+0.5*kvx1,vy+0.5*kvy1,t+0.5*dt)/m
    
    x+=kx2*dt
    vx+=kvx2*dt
    y+=ky2*dt
    vy+=kvy2*dt
    
    t+=dt
    
    if t>0:
        tlist.append(t)
        xlist.append(x)
        ylist.append(y)
        Elist.append(0.5*m*vx*vx+0.5*Dx*x*x+0.5*m*vy*vy+0.5*Dy*y*y)
    #print(t,x,v)
    
#Jules Antoine Lissajous emlékére 

#plt.plot(tlist, xlist, tlist, ylist)

plt.plot(xlist, ylist)
