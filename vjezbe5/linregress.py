import numpy as np
import math
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
fi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]


m_=0       
fi_=0
umn=0
for i in range(len(M)):
    m_+=((M[i])**2)
    fi_+=((fi[i])**2)
    umn+=(M[i]*fi[i])


m_kvadrat= m_ /len(M)
fi_kvadrat= fi_ /len(fi)
umnozak= umn/ len(M)

D=(umnozak / fi_kvadrat)
sigma=math.sqrt( (1/len(M))* (( m_kvadrat / fi_kvadrat) - D**2 ))
print(D)
print('Pogreška je ', sigma)

def graf(D, M, fi):
    plt.xlabel('fi [rad]')
    plt.ylabel('M [Nm]')
    plt.scatter(fi, M, label='Rezultati', color='red')

    y=[]
    for i in fi:
        y.append(D*i)

    plt.plot(fi, y,  label='Linearna regresija')
    plt.legend()
    plt.show()

graf(D, M, fi)