import calculus as c
import math
import matplotlib.pyplot as plt
import numpy as np

def fsin(x):
    return math.sin(x)
def sind(x):
    return math.cos(x)

def fcos(x):
    return math.cos(x)
def cosd(x):
    return -math.sin(x)
def fkub(x):
    return x**3
def kubd(x):
    return 3*x**2

#neki primjeri primjene i grafa na kubnu funkciju 

print(c.derivacija(fkub, 2, 0.0001)) 
print(c.pravokutna(fkub, 1,4,100))
print(c.trapezna(fkub, 1, 4, 100))

x=np.linspace(-2, 2, 100)
l1=c.tocke(fkub, -2, 2, 0.5)  #iznos derivacija od -2 do 2, h=0.5, c.tocke ce nam dati dvije liste, u jednoj su brojevi, u drugoj su vrijednosti derivacija za njih
l2=c.tocke(fkub, -2, 2, 0.0001)
l3=c.tocke(fkub, -2, 2, 0.01)

plt.title('Derivacija funkcije x^3')
plt.legend()
plt.xlabel('x')
plt.ylabel('df(x)/dx')
plt.plot(x, 3*(x**2))
plt.scatter(l1[0], l1[1], c='red', s=5)
plt.scatter(l2[0], l2[1], c='yellow', s=5)
plt.scatter(l3[0], l3[1], c='green', s=5)
plt.show()


