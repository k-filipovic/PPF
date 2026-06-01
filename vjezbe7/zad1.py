import numpy as np
np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02] # pogreske pri redukciji podataka


def histogram(podaci, k):
    x_min=min(podaci)
    x_max=max(podaci)
    h=(x_max-x_min)/k
    rubovi = []
    for i in range(k + 1):
        rub= x_min + i*h
        rubovi.append(rub)

    rj={         #stvaram dictionary

        } 
    
    for i in range(len(rubovi)-1):
        vrijednost=0
        for j in podaci:
            if j>=rubovi[i] and j<=rubovi[i+1]:
                kljuc=str(round(rubovi[i], 4))+' - '+ str(round(rubovi[i+1], 4))
                vrijednost+=1
                rj[kljuc]=vrijednost
    return rj
        

#crtanje grafa
import matplotlib.pyplot as plt

def graf(rjecnik):
    intervali= list(rjecnik.keys())
    frekvencije= list(rjecnik.values())
    plt.figure(figsize=(12, 6))
    plt.bar(intervali, frekvencije, color='lightblue', edgecolor='black', width=0.6)
    plt.xlabel('Razredi (Intervali masa)')
    plt.ylabel('Frekvencija (Broj podataka)')
    plt.title('Histogram masa')
    plt.xticks(rotation=45)
    plt.tight_layout()


if __name__ == "__main__":      #ovime sam samo osigurala da mogu zad1 upotrijebit kao modul jer se onda ne izvrsava ovaj dio zadatka
    rjecnik= histogram(mase_ciste, 10)
    graf(rjecnik)
    plt.show()
