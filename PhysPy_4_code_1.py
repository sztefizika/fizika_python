# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import time

start=time.time()

dt=0.01
D=1.0
D12=0.05
m=1.0
L=0.5
x10=0
x20=L
steps=0

t=0.0    
x1=0.3
v1=0.0
x2=L
v2=0.0

tlist=[t]
xlist1=[x1] #első tömgpont
vlist1=[v1]

xlist2=[x2] #második tömegppont
vlist2=[v2]


def F1(x1,x2):
    return -D*(x1-x10)+D12*(L-(x2-x1))

def F2(x1,x2):
    return -D*(x2-x20)-D12*(L-(x2-x1))

while t<200.0:
    # indexek (pl k12-nél: első: melyik k, második: melyik tömegpont) 
    
    kx11=v1*dt
    kv11=F1(x1,x2)/m*dt
    
    kx12=v2*dt
    kv12=F2(x1,x2)/m*dt
    
    kx21=(v1+0.5*kv11)
    kx22=(v2+0.5*kv12)
    
    kv21=F1(x1+0.5*kx11,x2+0.5*kx12)/m
    kv22=F2(x1+0.5*kx11,x2+0.5*kx12)/m
    
    x1+=kx21*dt
    v1+=kv21*dt
    
    x2+=kx22*dt
    v2+=kv22*dt
    
    steps+=1
    
    t+=dt
    
    if steps%20==0:
        tlist.append(t)
        xlist1.append(x1)
        vlist1.append(v1)
        xlist2.append(x2)
        vlist2.append(v2)
    
    
#plt.plot(tlist, xlist1, tlist, xlist2)
#plt.plot(tlist, vlist1, tlist, vlist2)
#plt.plot(tlist, Elist, tlist)

#videokeszites innentol

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='coupled oscillators', artist='none',
                comment='two dots representing interacting oscillators')
writer = FFMpegWriter(fps=30, metadata=metadata)

# Initialize the movie
fig = plt.figure()

zero_line1, = plt.plot([0,0], [0,210], 'black')
zero_line2, = plt.plot([0.5,0.5], [0,210], 'black')
x1_line, =plt.plot(xlist1,tlist)
x2_line, =plt.plot(xlist2,tlist)
red_circle, = plt.plot([], [], 'ro', markersize = 10)
blue_circle, = plt.plot([], [], 'bo', markersize = 10)
plt.xlabel('x')
plt.ylabel('t')
plt.axis([-0.3, 0.9, -3.2, 3.2])

# Update the frames for the movie
with writer.saving(fig, "csatolt.mp4", 100):
    for i in range(700):
        plt.axis([-0.4, 0.9, -3.2+i*20*dt, 3.2+i*20*dt])
        X1 = xlist1[i]
        X2=xlist2[i]
        y0 = i*dt*20
        red_circle.set_data(X1, y0)
        blue_circle.set_data(X2, y0)
        writer.grab_frame()



stop=time.time()

print("Futásidő:", '%.3f' % (stop-start), " s")

