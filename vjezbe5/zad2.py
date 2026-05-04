n=int(input('Upišite broj iteracija'))

def f (n):
    x=5
    for i in range(n):
        x+=(1/3)
    for j in range(n):
        x-=(1/3)
    return x

print(f(n))   