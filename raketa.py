import matplotlib.pyplot as plt
import math
import numpy as np

MODEL_G = 9.81
MODEL_DT = 0.001

class Body:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.trajectory_x = []
        self.trajectory_y = []
    

    def advance(self):
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT
        if self.y <= 0.0:
            self.vy = 0
            self.vx = 0
        
       

class Rocket(Body):
    def __init__(self, x, y):

        super().__init__(x, y, 8, 8) # Вызовем конструктор предка — тела, т.к. он для ракеты актуален
        self.raketa_mass = 50
        self.power_mass = 3
        self.rasxod = 1
        self.gazv = 300
  

    def advance(self):
        super().advance() # вызовем метод предка — тела, т.к. и он для ракеты актуален.
        if self.power_mass > 0.0:
            self.vy += (self.gazv * self.rasxod) / (self.raketa_mass + self.power_mass) * self.vy / math.sqrt(self.vx * self.vx  + self.vy * self.vy) # ускорение зависимое от направления ракеты
            self.vx += (self.gazv * self.rasxod) / (self.raketa_mass + self.power_mass) * self.vx / math.sqrt(self.vx * self.vx  + self.vy * self.vy)
            self.power_mass -= self.gazv
      
       


G = Body(3, 0, 15, 16)
b = Body(2, 0, 15, 16)
r = Rocket(0, 0)
bodies = [b, G, r]
rockets = [r]

for t in np.r_[0:5:MODEL_DT]: # для всех временных отрезков
    for b in bodies: # для всех тел
        b.advance() # выполним шаг


from matplotlib import pyplot as pp

for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y, color = 'red') # нарисуем их траектории
    
for b in rockets: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y, color = 'blue') # нарисуем их траектории
    
plt.grid(True)
plt.show()
