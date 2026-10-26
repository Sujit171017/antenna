#lab-03
# Horn Antenna-2D
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi/2, np.pi/2, 400)
n = 6
R = np.abs(np.cos(theta))**n

ax = plt.subplot(111, projection="polar")
ax.plot(theta, R)
ax.set_title("Horn Antenna (2D)")
plt.show()