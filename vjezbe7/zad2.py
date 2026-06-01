from zad1 import histogram
from zad1 import graf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02] # pogreske pri redukciji podataka

rjecnik=histogram(mase, 10)
graf(rjecnik)

mase_array= np.array(mase)
sr=np.mean(mase_array)
medijan=np.median(mase_array)
plt.axvline(x=sr, color='red', label='Aritmetička sredina', lw=2)
plt.axvline(x=medijan, color='purple', label='Medijan', linestyle='--', lw=2)
plt.legend()
plt.show()


