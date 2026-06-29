import matplotlib.pyplot as plt
from tema11 import Projectile 
import numpy as np

v=35
k=0
m=0.1
x=0
y=0
oblik='kugla'
ra=0.12
projektil = Projectile(v, k, m, x, y, oblik=oblik, ra=0.1)

xM=15
yM=3
rM=1
lista_kuteva= projektil.pronadji_kut(xM, yM, rM)

#moramo vidjeti postoje li dva rješenja, jedno ili nijedno
niska_putanja = []
visoka_putanja = []
niska_sr=None
visoka_sr=None

if len(lista_kuteva) > 0:
    # Prvi nađeni kut je uvijek početak niske putanje
    niska_putanja.append(lista_kuteva[0])
    
    # Prolazimo kroz ostale kutove iz liste i gledamo ima li skoka (visoke putanje)
    for k_tren in lista_kuteva[1:]:
        if k_tren - niska_putanja[-1] > 0.5:
            visoka_putanja.append(round(float(k_tren), 1))
        else:
            # Ako nema skoka, ovo je i dalje dio istog (prvog) niza kutova
            niska_putanja.append(round(float(k_tren), 1))


#nema rjesenja
if len(lista_kuteva)==0:
    print("Projektil ne doseže metu")

#Imamo i nisku putanju i visoku putanju nakon skoka
elif len(niska_putanja)>0 and len(visoka_putanja)>0:
    print("Meta je unutar dometa (Dva rješenja)")
    print(f"Niska putanja (kutovi): od {niska_putanja[0]}° do {niska_putanja[-1]}°")
    print(f"Visoka putanja (kutovi): od {visoka_putanja[0]}° do {visoka_putanja[-1]}°")
    niska=np.array(niska_putanja)
    visoka=np.array(visoka_putanja)
    niska_sr=round(np.mean(niska), 1)    #aritmeticka sredina kuteva da ne uzimamo svaki od njih(slicni kutevi)
    visoka_sr=round(np.mean(visoka), 1)

#Jedno rjesenje
else:
    print('Meta je unutar dometa (Jedinstveno rješenje)')
    print(f'Raspon kutova za pogodak: od {niska_putanja[0]}° do {niska_putanja[-1]}°')
    niska=np.array(niska_putanja)
    niska_sr=round(np.mean(niska), 1)

#GRAF 
if niska_sr is not None and visoka_sr is not None:
    projektil_1=Projectile(v, niska_sr, m, x, y, oblik=oblik, ra=0.1)
    x_1, y_1=projektil_1.graf()
    projektil_2=Projectile(v, visoka_sr, m, x, y, oblik=oblik, ra=0.1)
    x_2, y_2=projektil_2.graf()

    plt.figure(figsize=(10, 6))
    plt.title('Projektil i meta (dva rješenja)')
    plt.xlabel('Domet $(x / m)$')
    plt.ylabel('Visina $(y / m)$')
    plt.plot(x_1, y_1, label=f'Projektil manjeg kuta (\u03b8 ={niska_sr}°)', color='blue', linewidth=2)
    plt.plot(x_2, y_2, label=f'Projektil većeg kuta (\u03b8 ={visoka_sr}°)', color='pink', linewidth=2)
    meta = plt.Circle((xM, yM), rM, color='yellow', alpha=0.5, label='Meta')
    plt.gca().add_patch(meta)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid()
    plt.show()

elif visoka_sr is None and niska_sr is not None:
    projektil_1=Projectile(v, niska_sr, m, x, y, oblik=oblik, ra=0.1)
    x_1, y_1=projektil_1.graf()

    plt.figure(figsize=(10, 6))
    plt.title('Projektil i meta (jedno rješenje)')
    plt.xlabel('Domet $(x / m)$')
    plt.ylabel('Visina $(y / m)$')
    plt.plot(x_1, y_1, label=f'Projektil (\u03b8 ={niska_sr}°)', color='blue', linewidth=2)
    meta = plt.Circle((xM, yM), rM, color='yellow', alpha=0.5, label='Meta')
    plt.scatter(xM, yM, s=0.1, alpha=0.001)
    plt.gca().add_patch(meta)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid()
    plt.show()
else:    
    plt.figure(figsize=(10, 6))
    plt.title('Projektil i meta (nema rješenja)')
    plt.xlabel('Domet $(x / m)$')
    plt.ylabel('Visina $(y / m)$')
    plt.scatter(xM, yM, s=10, alpha=0.5, color='yellow')
    plt.grid()
    plt.show()