#Otto cycle simulator

import math
import matplotlib.pyplot as plt

def final_egineKine(bore,stroke, con_rod,cr, start_crank,end_crank):



	#geometric parameters
	a = stroke/2
	R = con_rod/a

	#Volume parmaeters
	v_s = math.pi*(1/4)*pow(bore,2)*stroke
	v_c = v_s/(cr-1)

	sc = math.radians(start_crank)
	ec = math.radians(end_crank)

	num_values = 50
	dtheta = (ec - sc)/(num_values-1)

	v = []

	for i in range(0,num_values):
		theta = sc + i*dtheta
		term1 = 0.5*(cr-1)
		term2 = R + 1 - math.cos(theta)
		term3 = pow(R,2) - pow(math.sin(theta),2)
		term3 = pow(term3,0.5)

		v.append((1 + term1*(term2- term3))*v_c)

	return v


#inputs
p1 = 101325
t1 = 500
gamma = 1.4
t3 = 2300

#geometric parameters
bore = 0.1
stroke = 0.1
con_rod = 0.15
cr = 12


#Volume computation
v_s = (math.pi/4)*pow(bore,2)*stroke
v_c = v_s/(cr-1)
v1 = v_c + v_s


#state point 2
v2 = v_c

#p2v2^gamma = p1v1^gamma
p2 = p1*pow(v1,gamma)/pow(v2,gamma)

#p2v2/t2 = p1v1/t1| rhs = p1v1/t1| p2v2/t2 = rhs| t2 = p2v2/rhs
rhs = p1*v1/t1
t2 = p2*v2/rhs
v_compression = final_egineKine(bore,stroke,con_rod,cr,180,0)

constant = p1*pow(v1,gamma)

P_compression = []

for v  in v_compression:
	P_compression.append(constant/pow(v,gamma))

#State point 3
v3 = v2

#p3v3/t3 = p2v2/t2| rhs = p2v2/t2 | p3 = rhs*t3/v3
rhs= p2*v2/t2
p3 = rhs*t3/v3

v_expansion = final_egineKine(bore,stroke,con_rod,cr,0,180)

constant = p3*pow(v3,gamma)

P_expansion = []
	
for v  in v_expansion:
	P_expansion.append(constant/pow(v,gamma))

#state point 4
v4 = v1

#p4v4^gamma = p3v3^gamma

p4 = p3*pow(v3,gamma)/pow(v4,gamma)


#p4v4/t4 = rhs
t4 = p4*v4/rhs

#Thermal efficiency of the engine
eff1 = 1-(t4 -t1)/(t3 - t2)
Efficiency = eff1*100
print(Efficiency)

plt.plot([v2,v3],[p2,p3])
plt.plot(v_compression, P_compression)
plt.plot(v_expansion, P_expansion)
plt.plot([v4,v1],[p4,p1])
plt.xlabel('Pressure(Mpa)')
plt.ylabel('Volume(m3)')
plt.title('Figure1:P-V Diagram')
plt.show()


