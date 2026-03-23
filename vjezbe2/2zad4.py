import math
import calculus as c
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x**2+3

print('gornja i donja integralna suma su: ', c.pravokutna(f, 0, 1, 100))  
print('integral pomoću trapeza ', c.trapezna(f, 0, 1, 100))

n=np.arange(50, 501, 20)    #stvaramo arange za n podjela koji će biti na x osi
x=np.linspace(50, 501, 200)     #ovo nam treba samo za crtanje pravca analitičkog integrala
y=np.linspace(11/3, 11/3, 200)  #ovo je vrijednost integrala kojeg sam odabrala
n=n.tolist()    #stavljam n-ove u listu
trapezni=[] #lista sa vrijednostima trapeznog integrala
pgornji=[]  #pravokutni gornji
pdonji=[]   #pravokutni donji 
for i in n:     #petlja za listu trapeznih
    k=c.trapezna(f, 0, 1, i)
    trapezni.append(k)
for j in n:
    u=c.pravokutna(f, 0, 1, j)
    pgornji.append(u[0])
    pdonji.append(u[1])

plt.title('Derivacija funkcije x^3')
plt.legend()
plt.xlabel('n')
plt.ylabel('Integral')
plt.plot(x, y)
plt.scatter(n, trapezni, s=5)
plt.scatter(n, pgornji, s=5)
plt.scatter(n, pdonji, s=5)
plt.show()
