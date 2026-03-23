import math 
class particle:
    def __init__(self, v, k, xy):
        self.v=v
        self.k=math.radians(k)
        self.xy=xy
        self.x=xy[0]
        self.y=xy[1]
        self.x_list = [self.x]   #pravim listu u koju ce se poslije spremati x
        self.y_list = [self.y]
        self.vx=v*math.cos(self.k)
        self.vy=v*math.sin(self.k)
        
    def reset(self):
        self.v=0
        self.k=0
        self.xy=[0,0]

    def __move(self, dt):       #privatna metoda koju ćemo koristiti poslije 
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.g=9.81
        self.vy -= self.g * dt
        self.x_list.append(self.x)
        self.y_list.append(self.y)

    def range(self):
        dt=0.05
        while self.y >= 0:      #pomićemo česticu sve dok ne padne na tlo za neki dt
            self.__move(dt)
        return self.x
    
    def plot_trajectory(self):
        import matplotlib.pyplot as plt
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('Gibanje čestice')
        plt.plot(self.x_list, self.y_list)
        return plt.show()

        