#lab-01
# Write a program to draw a raditation pattern of dipole Antenna 
# Dipole Antenna-2D 
import numpy as np
import matplotlib.pyplot as plt

# Angle values (0 to 180 degree)
theta = np.linspace(0, np.pi, 360)

# Radiation pattern
R = np.abs(np.sin(theta))

# Polar plot
plt.figure()
ax = plt.subplot(111, projection='polar')
ax.plot(theta, R)

ax.set_title("2D Radiation Pattern of Dipole Antenna", va='top')
plt.show()