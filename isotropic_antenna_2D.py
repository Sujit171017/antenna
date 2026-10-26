#lab-02
# Isotropic Antenna- 2D 
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 400)
R = np.ones_like(theta)

ax = plt.subplot(111, projection="polar")
ax.plot(theta, R)
ax.set_title("Isotropic Antenna (2D)")
plt.show()