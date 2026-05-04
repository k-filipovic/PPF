import numpy as np
import math

b= list(map(float, input("Unesite 10 točaka: ").split(', ')))
b=np.array(b)
print(b)
sr=np.mean(b)
dev=np.std(b, ddof=1)/math.sqrt(len(b))
print(sr)
print(dev)