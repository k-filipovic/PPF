import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

g=9.81
kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
kut_rad=np.radians(kut_deg)
T_120 = np.array([0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653, 0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373, 1.9100, 2.5460])
T_240 = np.array([1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720, 1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840, 2.4473, 3.1573])


def period(theta, l):        #curve_fit ne moze raditi ako u formuli nema barem jedne nepoznanice koju mora otkriti, uvodimo l koji treba naci
    return 2* np.pi * np.sqrt(l / (g * np.cos(theta)))

l_teorijski_120=0.120
popt_120, pcov = curve_fit(period, kut_rad, T_120)    #linija potpomognuta AI-em 
#popt (Optimalni parametri), pcov (Matrica kovarijance)
l_120= popt_120[0]  #fit vraća popis svih pronađenih rješenja, redoslijedom kojim su napisani u definiciji funkcije (def) 
pogreska_120 = (abs(l_120 - l_teorijski_120) / l_teorijski_120) * 100
print("Relativna pogreška za L=120mm iznosi:", pogreska_120, "%")

l_teorijski_240=0.240
popt_240, pcov = curve_fit(period, kut_rad, T_240)
l_240 = popt_240[0]
pogreska_240 = (abs(l_240 - l_teorijski_240) / l_teorijski_240) * 100
print("Relativna pogreška za L=240mm iznosi:", pogreska_240, "%")

#GRAF
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
x = np.linspace(0, 85, 200)
x_rad= np.radians(x)

#lijevi graf, L=120mm
teorijski_T_120 = period(x_rad, l_120)
T1= period(x_rad, 0.120)
ax1.scatter(kut_deg, T_120, color='red', label='Mjerenja (120 mm)')
ax1.plot(x, teorijski_T_120, color='blue', label='Teorijski model')
ax1.plot(x, T1, color='blue', label='Idealni model')
ax1.set_title('Njihalo L = 120 mm')
ax1.set_xlabel('Kut otklona (stupnjevi)')
ax1.set_ylabel('Period T(s)')
ax1.grid()
ax1.legend()

#desni graf, L=240mm
teorijski_T_240 = period(x_rad, l_240)
T2= period(x_rad, 0.120)
ax2.scatter(kut_deg, T_240, color='orange', label='Mjerenja (240 mm)')
ax2.plot(x, teorijski_T_240, color='green', label='Teorijski model')
ax2.plot(x, T2, color='green', label='Teorijski model')
ax2.set_title('Njihalo L = 240 mm')
ax2.set_xlabel('Kut otklona (stupnjevi)')
ax2.set_ylabel('Period T(s)')
ax2.grid()
ax2.legend()
plt.tight_layout()
plt.show()
