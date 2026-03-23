def derivacija(f, x, h, m='three-step'):
    if m=='three-step':
        return round((f(x+h) - f(x-h))/(2*h), 4)
    elif m=='two-step':
        return round((f(x+h)-f(x))/(h), 4)
    else:
        raise ValueError ('Metoda mora biti three-step ili two-step')

def tocke(f, a, b, h):
    import numpy as np
    br=np.arange(a, b +0.1, 0.1)
    br=br.tolist()
    der=[]
    for j in br:
        d=(f(j+h)-f(j-h))/(2*h)
        der.append(round(d, 4))

    return [br, der]

def pravokutna(f, a, b, n):
    dx=(b-a)/n
    g=0     #gornja suma
    d=0     #donja suma
    for i in range(n):
        d+= f(a+i*dx)*dx
        g+= f(a+(i+1)*dx)*dx
    return [round(g, 4), round(d, 4)]
    
def trapezna(f, a, b, n):
    dx=(b-a)/n
    s=0
    for i in range (n):
        s+=f(a+dx*i)+f(a+dx*(i+1))
    return round(s*dx/2, 4)

