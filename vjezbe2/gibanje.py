import particle as prt
import math
p=prt.particle(10, 45, [1, 2])
d_n=p.range()
d_a=12.9066  #analiticki izracunat rezultat za dane koordinate

print('Razlika u računu je ', round(d_n-d_a, 4), 'm.')

p.plot_trajectory()

