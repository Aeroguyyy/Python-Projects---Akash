#Otto cycle simulator

import math
import matplotlib.pyplot as plt

#Inputs
p1 = 101325
t1 = 500
t3 = 2300
gamma = 1.4

#geometric parameters
bore = 0.10
stroke = 0.1
con_rod = 0.15
cr = 12
a = stroke/2
R = con_rod/a

#Volume parmaeters
v_s = math.pi*(1/4)*pow(bore,2)*stroke
v_c = v_s/(cr-1)

theta = math.radians(0)

term1 = 0.5*(cr-1)
term2 = R + 1 - math.cos(theta)
term3 = pow(R,2) - pow(math.sin(theta),2)
term3 = pow(term3,0.5)

v = (1 + term1*(term2- term3))*v_c

print(v_c)
print(v)