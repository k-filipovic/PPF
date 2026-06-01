import numpy as np
np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02] # pogreske pri redukciji podataka
mase_array= np.array(mase)     #niz masa

sr_mase=np.mean(mase_array)
med_mase=np.median(mase_array)

print(sr_mase)
print(med_mase)
print('Razlika sredine i medijana:', sr_mase-med_mase)

std_mase = np.std(mase_array)   #gledamo standardnu devijaciju
mase_nova=[]
for i in mase:
    if abs(i-sr_mase) < (2*std_mase):       #podaci koji od sredine odstupaju za manje od 2 standardne devijacije, matematicki dogovor
        mase_nova.append(i)

nova_array=np.array(mase_nova)     #niz masa bez vrijednosti koje previse odskacu

sr_nova=np.mean(nova_array)
med_nova=np.median(nova_array)

print(sr_nova)
print(med_nova)

print('srednja vrijednost se smanjuje za', (sr_mase-sr_nova))
print('Medijan se smanjuje za', (med_mase - med_nova))

#očekivano, sredina se smanjuje više nego medijan

import matplotlib.pyplot as plt
plt.hist(mase_array, color='lightpink', label='Zadane mase')
plt.hist(nova_array, color='yellow', label='Mase bez odstupanja')
plt.axvline(x=sr_mase, color='red', label='Aritmetička sredina', lw=2)
plt.axvline(x=med_mase, color='blue', label='Medijan', lw=2)
plt.axvline(x=sr_nova, color='red', label='Aritmetička sredina bez odstupanja', linestyle='--', lw=2)
plt.axvline(x=med_nova, color='blue', label='Medijan bez odstupanja', linestyle='--', lw=2)
plt.legend()
plt.show()

print('Medijan bolje procjenjuje masu zvijezda')
