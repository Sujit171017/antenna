#lab-8
# unequal amplitude any opposite phase
import numpy as np
import matplotlib.pyplot as plt

# Parameters
lam = 1.0                 # wavelength (normalized)
d = lam / 2               # spacing
k = 2 * np.pi / lam       # wave number

A1 = 1.0                  # Amplitude of source 1
A2 = 0.6                  # Amplitude of source 2 (UNEQUAL)

# Angle range
theta = np.linspace(0, 2*np.pi, 1000)

# Phase term
psi = (k * d / 2) * np.cos(theta)

# Array Factor (unequal amplitude, opposite phase)
AF = A1 * np.exp(1j * psi) - A2 * np.exp(-1j * psi)

# Normalized magnitude
AF_norm = np.abs(AF) / np.max(np.abs(AF))

# Polar plot
plt.figure(figsize=(6,6))
plt.polar(theta, AF_norm)
plt.title("Far-Field Pattern\nTwo Isotropic Point Sources\nUnequal Amplitude & Opposite Phase\n\n")
plt.show()