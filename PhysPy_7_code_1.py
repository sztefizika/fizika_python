# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')



N=50
Nk=100
Z=np.zeros(shape=(Nk,Nk))
ertek=np.zeros(20)
hatarok=np.zeros(21)
sugarak=np.zeros(6)
szoglepes=2.0*np.pi/20.0
start=-0.5*szoglepes

sigma=2.0

for i in range(21) :
    hatarok[i]=i*szoglepes

sugarak[0]=0.635
sugarak[1]=1.6
sugarak[2]=9.9
sugarak[3]=10.7
sugarak[4]=16.2
sugarak[5]=17

pontok=np.linspace(-sugarak[5],sugarak[5],N)
kozepx=np.linspace(-sugarak[5],sugarak[5],Nk)
kozepy=np.linspace(sugarak[5],-sugarak[5],Nk)


ertek[0]=6
ertek[1]=13
ertek[2]=4
ertek[3]=18
ertek[4]=1
ertek[5]=20
ertek[6]=5
ertek[7]=12
ertek[8]=9
ertek[9]=14
ertek[10]=11
ertek[11]=8
ertek[12]=16
ertek[13]=7
ertek[14]=19
ertek[15]=3
ertek[16]=17
ertek[17]=2
ertek[18]=15
ertek[19]=10

# Hany pontot kapunk, ha a nyilunk az (x,y) pontot talalja el?
def eredmeny(x,y):
    szog=np.arctan2(y,x)-start

    if szog<0:
        szog+=2.0*np.pi
    sugar=np.sqrt(x*x+y*y)
    
    if sugar<sugarak[0]:
        return(50)
    
    if sugar<sugarak[1]:
        return(25)
    
    if sugar>sugarak[5]:
        return(0)
    
    for i in range(21) :
        if szog<hatarok[i]:
            break
    sector=ertek[i-1]
    
    if (sugar>sugarak[2])and(sugar<sugarak[3]):
        return(3*sector)
    
    if (sugar>sugarak[4])and(sugar<sugarak[5]):
        return(2*sector)
    
    return(sector)

print('tripla 20?', eredmeny(0,(sugarak[3]+sugarak[2])/2))    


# A ketdimenzios P fuggveny, x0, y0 a centrum
def valszin(x0,y0,x,y,sigma):
    exponens=-((x-x0)*(x-x0)+(y-y0)*(y-y0))/(2*sigma*sigma)
    prefactor=1/(2*np.pi*sigma*sigma)
    return(prefactor*np.exp(exponens))

# Varhato ertek, ha az (x0,y0) pontra celzunk sigma szorassal
def varhato(x0,y0,sigma):
    varh=0
    for i in range(N):
        for j in range(N):
            varh+=valszin(x0,y0,pontok[i],pontok[j],sigma)*eredmeny(pontok[i],pontok[j])
    varh*=4*sugarak[5]*sugarak[5]/N/N
    return(varh)

    
sigma=2.0

max=0
 
#kiszamoljuk az abra adatait   
for i in range(Nk):
    for j in range(Nk):
        x0=kozepx[i]
        y0=kozepy[j]
        Z[j][i]=varhato(x0,y0,sigma)
        if Z[j][i]>max:
            max=Z[j][i]
                
print("Max varhato ertek",max)

#abrazolunk   
c=plt.imshow(Z)
plt.colorbar(c)
plt.axis('off')
plt.title("szigma="+str(sigma))
plt.show



