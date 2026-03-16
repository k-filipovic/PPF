
def jednoliko_gibanje(F, m):
    import numpy as np
    import matplotlib.pyplot as plt
    a=F/m
    dt=0.1 
    t=np.arange(0, 10+dt, dt)

    v = np.zeros_like(t)  #niz iste duljine s vrijednostima 0 (chatgpt)
    x = np.zeros_like(t)

    for i in range(1, len(t)):   #nismo ucili numericki pristup i eulerove formule ali mi je chatgpt napravio 
        v[i] = v[i-1] + a*dt   
        x[i] = x[i-1] + v[i-1]*dt  


    plt.figure(figsize=(12, 8))

    plt.subplot(1,3,1)
    plt.plot(t, x)
    plt.ylabel('x')
    plt.xlabel('t')
    plt.title('x(t)')

    plt.subplot(1,3,2)
    plt.plot(t, v)
    plt.ylabel('v')
    plt.xlabel('t')
    plt.title('v(t)')

    ac=[]
    for i in range(len(t)):
        ac.append(a)

    plt.subplot(1,3,3)
    plt.plot(t, ac)
    plt.ylabel('a')
    plt.xlabel('t')
    plt.title('a(t)')

    plt.tight_layout()
    plt.show()