import math
h0 = 0.54
# m
m = 0.5257
# kg
r = 4.025e-3 # m

h= [0.14, 0.17, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34, 0.37, 0.40]# m
t_mean = [1.740, 1.793, 2.043, 2.190, 2.280, 2.417, 2.540, 2.640, 2.670, 2.813]


def logaritmi(lista):
    nova=[]
    for i in lista:
        x=math.log(i, 10)   #logaritam po bazi 10
        nova.append(x)
    return nova

h_log=logaritmi(h)      #y
t_log=logaritmi(t_mean) #x

def a(x, y):
    s1=0
    for i in range(len(x)):
        s1+=x[i]*y[i]
    s2=0
    for i in x:
        s2+=i**2
    n=len(x)
    a=(n*s1 - (sum(x)*sum(y))) / (n*s2 - (sum(x))**2)
    return a

koef_a =a(t_log, h_log)

def b(x, y, a):
    b=(sum(y) - a*sum(x)) / len(x)
    return b

koef_b =b(t_log, h_log, koef_a)

import matplotlib.pyplot as plt
import numpy as np
plt.scatter(t_log, h_log, color='purple', label='Točke mjerenja')
x = np.linspace(0.1, 0.6, 100)
y = koef_a*x + koef_b
plt.plot(x, y, label='Linearizirani pravac')
plt.xlabel('$log(t)$')
plt.ylabel('$log(s)$')
plt.legend()
plt.show()

print('a=', koef_a)
print('b=', koef_b)

def standardna_pogreska(x, y, a, b):    #formula za sigumu, AI
    s=0
    for i in range(len(x)):
        s+=(y[i]-(a*x[i])-b)**2
    sigma=math.sqrt((s) / (len(x)-2))
    return sigma
sigma=standardna_pogreska(t_log, h_log, koef_a, koef_b)

def s_a(sigma, x):      #sigma za a
    s=0
    sredina=np.mean(x)
    for i in x:
        s+=(i-sredina)**2
    sa=sigma / math.sqrt(s)
    return sa

sigma_a =s_a(sigma, t_log)

def s_b(sigma_a, x):
    s=0
    for i in x:
        s+=i**2
    s_b=sigma_a * (math.sqrt(s/len(x)))
    return s_b

sigma_b=s_b(sigma_a, t_log)

print('Standardna pogreška je ', sigma, ', pogreška za a je ', sigma_a, ', a pogreška za b je', sigma_b)
