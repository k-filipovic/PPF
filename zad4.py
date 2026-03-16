x1=input('upisite x koorfinatu prve tocke')
y1=input('upisite y koordinatu prve tocke')
x2=input('upisite x koorfinatu druge tocke')
y2=input('upisite y koordinatu druge tocke')
k1=[x1, y1]
k2=[x2, y2]

def tocke(k1, k2):
    k=(float(y2)-float(y1))/(float(x2)-float(x1))
    l=float(y1)-k*float(x1)
    s='y='+str(k)+'x+'+str(l)
    return s
print(tocke(k1, k2))