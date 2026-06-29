import math
import numpy as np

class Projectile:
    def __init__(self, v, k, m, x, y, rho=1.225, oblik='kugla', ra=0.06):   #rho = 1.225, standardna gustoća zraka na razini mora(15°C)
        self.k=math.radians(k)
        self.m=m
        self.ra=ra
        self.rho=rho

        #postavljamo velicine s obzirom na izbor korisnika
        self.oblik = oblik.lower()    #samo osigurava da su slova uvijek mala
        if self.oblik == "kugla":
            self.A= (self.ra**2) * math.pi
            self.c= 0.47
        elif self.oblik== "kocka":
            self.A= self.ra**2
            self.c= 1.05
        else:
            raise ValueError("Nedozvoljen oblik! Odaberite 'kugla' ili 'kocka'.")
        self.x0=x
        self.y0=y
        self.v0=v
        self.vx0=v*math.cos(self.k)
        self.vy0=v*math.sin(self.k)

        self.x=x
        self.y=y
        self.vx=v*math.cos(self.k)
        self.vy=v*math.sin(self.k)

        self.x_r4= [self.x]    #pravim liste u koje ce se poslije spremati x, y
        self.y_r4= [self.y]


    def __b(self, vx, vy):               #Funkcija koja računa trenutni otpor zraka
        if self.oblik == "kugla":
            A = (self.ra**2) * math.pi   #Za kuglu poprečni presjek uvijek krug
        elif self.oblik == "kocka":   
            if vx!= 0:
                theta= math.atan2(vy, vx)
            else:
                theta= math.pi / 2       #vertikalno gibanje jer tangens nije definiran za pi/2
            #Projekcija kocke koja se ne rotira na ravninu okomitu na smjer gibanja
            A= (self.ra**2)* (abs(math.cos(theta)) + abs(math.sin(theta)))   
            #Apsolutna jer kutevi mogu biti i negativni 
            
        return (0.5 * self.rho * self.c * A)     


    def __R4(self, dt):
        g=9.81
        #k1
        v1=np.sqrt(self.vx**2+self.vy**2)
        b1=self.__b(self.vx, self.vy)
        ax1=-(b1/self.m)*v1*self.vx
        ay1=-g-(b1/self.m)*v1*self.vy

        #k2
        vx2= self.vx + ax1*dt/2
        vy2= self.vy + ay1*dt/2
        v2= np.sqrt(vx2**2+vy2**2)
        b2=self.__b(vx2, vy2)
        ax2= -(b2/self.m)*v2*vx2
        ay2= -g-(b2/self.m)*v2*vy2

        #k3
        vx3= self.vx + ax2*dt/2
        vy3= self.vy + ay2*dt/2
        v3= np.sqrt(vx3**2+vy3**2)
        b3= self.__b(vx3, vy3)
        ax3= -(b3/self.m)*v3*vx3
        ay3= -g-(b3/self.m)*v3*vy3
    
        #k4
        vx4= self.vx + ax3*dt
        vy4= self.vy + ay3*dt
        v4= np.sqrt(vx4**2+vy4**2)
        b4= self.__b(vx4, vy4)
        ax4= -(b4/self.m)*v4*vx4
        ay4= -g-(b4/self.m)*v4*vy4

        #polozaj prema r4
        self.x=self.x+(dt/6)*(self.vx+2*vx2+2*vx3+vx4)
        self.y=self.y+(dt/6)*(self.vy+2*vy2+2*vy3+vy4)
    
        #brzina prema r4
        self.vx=self.vx+(dt/6)*(ax1+2*ax2+2*ax3+ax4)
        self.vy=self.vy+(dt/6)*(ay1+2*ay2+2*ay3+ay4)

        self.x_r4.append(self.x)
        self.y_r4.append(self.y)

    
    def graf(self):    
        dt=0.0001
        while self.y >= 0: 
            self.__R4(dt)
        return self.x_r4, self.y_r4
    
    def pronadji_kut(self, xM, yM, rM):
        kutovi_pogotka= []
        dt= 0.001
        g= 9.81
    
        v_ukupna =self.v0

        # Prolazimo kroz sve kutove od 0.5° do 89°
        kutovi= list(np.arange(0.5, 90.0, 0.1))
        for kut in kutovi:
            radijani = math.radians(kut)
            
            #nove liste za trenutni kut 
            testni_x = [self.x0]
            testni_y = [self.y0]
            
            #početni uvjeti za ovaj kut
            t_x = self.x0
            t_y = self.y0
            t_vx = v_ukupna * math.cos(radijani)
            t_vy = v_ukupna * math.sin(radijani)
            
            #sada sa R4 simuliramo let 
            while t_y >= 0:
                # k1
                v1 = np.sqrt(t_vx**2 + t_vy**2)
                b1 = self.__b(t_vx, t_vy)
                ax1 = -(b1 / self.m) * v1 * t_vx
                ay1 = -g - (b1 / self.m) * v1 * t_vy

                # k2
                vx2 = t_vx + ax1 * dt / 2
                vy2 = t_vy + ay1 * dt / 2
                v2 = np.sqrt(vx2**2 + vy2**2)
                b2 = self.__b(vx2, vy2)
                ax2 = -(b2 / self.m) * v2 * vx2
                ay2 = -g - (b2 / self.m) * v2 * vy2

                # k3
                vx3 = t_vx + ax2 * dt / 2
                vy3 = t_vy + ay2 * dt / 2
                v3 = np.sqrt(vx3**2 + vy3**2)
                b3 = self.__b(vx3, vy3)
                ax3 = -(b3 / self.m) * v3 * vx3
                ay3 = -g - (b3 / self.m) * v3 * vy3
            
                # k4
                vx4 = t_vx + ax3 * dt
                vy4 = t_vy + ay3 * dt
                v4 = np.sqrt(vx4**2 + vy4**2)
                b4 = self.__b(vx4, vy4)
                ax4 = -(b4 / self.m) * v4 * vx4
                ay4 = -g - (b4 / self.m) * v4 * vy4

                # Novi položaj i brzina
                t_x += (dt / 6) * (t_vx + 2 * vx2 + 2 * vx3 + vx4)
                t_y += (dt / 6) * (t_vy + 2 * vy2 + 2 * vy3 + vy4)
                t_vx += (dt / 6) * (ax1 + 2 * ax2 + 2 * ax3 + ax4)
                t_vy += (dt / 6) * (ay1 + 2 * ay2 + 2 * ay3 + ay4)

                testni_x.append(t_x)
                testni_y.append(t_y)
                
            #For petljom prolazimo kroz sve x, y i gledamo udaljenost
            pogodak = False
            for i in range(len(testni_x)):
                d= math.sqrt((testni_x[i] - xM)**2 + (testni_y[i] - yM)**2)  #udaljenost
                if d <= rM:
                    pogodak= True
                    kutovi_pogotka.append(round(float(kut), 1))
                    break # Čim nađemo jedan pogodak na ovoj putanji, prekidamo provjeru za ovaj kut
        
        return kutovi_pogotka

 