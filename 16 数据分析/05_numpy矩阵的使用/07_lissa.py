import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 2 * np.pi, 201)
print(t)
A, a, B, b = 10, 1, 5, 1

x = A * np.sin(a * t + np.pi / 2)
y = B * np.sin(b * t)

plt.figure("Lissajous", facecolor="lightgray")
plt.title("Lissajous", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.plot(x, y)

plt.show()
