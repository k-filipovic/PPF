b= list(map(float, input("Unesite 10 točaka: ").split(', ')))


def sredina(b):
    s=sum(b)
    sr=s/len(b)
    return sr

print(sredina(b))

def devijacija (b):
    import math
    s=sum(b)
    n=len(b)
    sr=s/n
    brojnik=0
    for i in b:
        brojnik+=(i-sr)**2
    dev=math.sqrt(brojnik/(n*(n-1)))
    return dev

print(devijacija(b))
