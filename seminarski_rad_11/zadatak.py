import matplotlib.pyplot as plt
from tema11 import Projectile 

v= 10       # m/s
kut= 45 # stupnjevi
m= 1         # kg
x0= 0
y0= 1
dim_kugla= 0.1     # r = 10 cm za kuglu, a = 10 cm za kocku
dim_kocka=0.2
#Stvaramo objekte pozivajući klasu koju smo importali
kugla = Projectile(v, kut, m, x0, y0, oblik="kugla", ra=0.1)
kocka = Projectile(v, kut, m, x0, y0, oblik="kocka", ra=0.2)

#Računamo putanje (koristeći R4 metodu)
x_kugla, y_kugla = kugla.graf()
x_kocka, y_kocka = kocka.graf()

#Zajednički graf
plt.figure(figsize=(10, 6))
plt.plot(x_kugla, y_kugla, label=f'Kugla (r={dim_kugla}m)', color='blue', linewidth=2)
plt.plot(x_kocka, y_kocka, label=f'Kocka (a={dim_kocka}m)', color='red', linestyle='--', linewidth=2)
plt.xlabel('Domet $(x / m)$')
plt.ylabel('Visina $(y / m)$')
plt.title('Usporedba putanje kugle i kocke s otporom zraka', size=14)
plt.grid(True, alpha=0.6)
plt.legend()

# Prikaz grafa
plt.show()
