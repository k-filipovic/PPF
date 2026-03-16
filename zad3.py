x1=input('upisite x koorfinatu prve tocke')
y1=input('upisite y koordinatu prve tocke')
x2=input('upisite x koorfinatu druge tocke')
y2=input('upisite y koordinatu druge tocke')

if iter(x1)!=float or iter(y1)!=float or iter(x2)!=float or iter(y2)!=float:
    print('ponovite upis')

k=((y2-y1)/(x2-x1))
l=y1-k*x1

print('y=', k, 'x+',l )