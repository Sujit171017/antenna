#lab-6
import numpy as np
import matplotlib.pyplot as plt

# Parameters
lam = 1.0                 # wavelength (normalized)
d = lam / 2               # element spacing
k = 2 * np.pi / lam       # wave number

# Angle range
theta = np.linspace(0, 2*np.pi, 1000)

# Array Factor (equal amplitude & phase)
AF = 2 * np.cos((k * d / 2) * np.cos(theta))

# Normalized magnitude
AF_norm = np.abs(AF) / np.max(np.abs(AF))

# Plot (Polar)
plt.figure(figsize=(6,6))
plt.polar(theta, AF_norm)
plt.title("Far-Field Pattern\nTwo Isotropic Point Sources\nEqual Amplitude & Phase (d = λ/2)\n\n")
plt.show()