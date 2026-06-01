a = [3, 1, 4, 1, 5, 9, 2, 6] # paran n
b = [3, 1, 4, 1, 5, 9, 2, 6, 5] # neparan n

def medijan(podaci):
    p=sorted(podaci)
    if (len(p)%2)==0:        #parni
        i1=len(p)//2
        i2=i1+1
        x=(p[i1]+p[i2])/2
    else:
        i=(len(p)+1)//2
        x=p[i]
    return x

print('medijan od a:', medijan(a))
print('medijan od b:', medijan(b))

import numpy as np
np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02] # pogreske pri redukciji podataka
mase_array= np.array(mase)

print('medijan od mase (rucno):', medijan(mase))
print('medijan od mase (gotovi modul):', np.median(mase_array))
