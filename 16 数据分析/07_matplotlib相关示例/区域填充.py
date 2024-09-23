import numpy as np
import matplotlib.pyplot as plt


n = 1000
x = np.linspace(0, 8 * np.pi, n)
sin_y = np.sin(x)
cos_y = np.cos(x/2)/2

plt.figure("Scatter", facecolor="lightgray")
plt.title("Scatter", fontsize=20)

plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.tick_params(labelsize=10)
plt.grid(linestyle=":")

plt.plot(x, sin_y, c="dodgerblue", label=r"$y=sin(x)$")
plt.plot(x, cos_y, c="orange", label=r"$y=\frac{1}{2}cos(\frac{x}{2})$")

plt.fill_between(x, cos_y, sin_y, cos_y < sin_y, color="pink", alpha=.5)

plt.show()