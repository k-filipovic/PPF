import math
h0 = 0.54
# m
m = 0.5257
# kg
r = 4.025e-3 # m
g=9.81

h= [0.14, 0.17, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34, 0.37, 0.40]# m
t_mean = [1.740, 1.793, 2.043, 2.190, 2.280, 2.417, 2.540, 2.640, 2.670, 2.813]


def t_kv(t):
    nova=[]
    for i in t:
        nova.append(i**2)
    return nova

t_kvadrat=t_kv(t_mean)

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

koef_a =a(t_kvadrat, h) 
a_ef = koef_a*2   #nagib pravca jednak je a_ef / 2

I= ( (m*g*(r**2))/a_ef ) - m*(r**2)
print('Moment tromosti je ', I)