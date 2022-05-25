#Calculate the drag force on the bicycle


#CASE 1

import matplotlib.pyplot as plt

#Inputs

#V1 = 25

#Drag Coefficient
c_d = 0.8

#Frontal area (m^2)
A = 0.1

#Density (kg/m^3)
rho = 1.25

#Bicycle Velocity 
velocities = [5,6,7,8,9,10,11,12]
drag_forces = []

for velocity in velocities:
	drag_forces.append(0.5*rho*A*c_d*velocity*velocity)

plt.plot(velocities,drag_forces)
plt.xlabel('Velocities(m/s)')
plt.ylabel('Drag forces(N)')
plt.title('Figure1: Velocity Vs Drag force')
plt.show()
print(drag_forces)

