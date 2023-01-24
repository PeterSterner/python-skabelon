import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = []
    for v in x:
        y.append(np.sqrt(1-np.power(v,2)))
    return y

fig = plt.figure()
ax = plt.axes()
ax.set_aspect('equal', adjustable='box')

a = -1
b = 1
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, color='red', linestyle='-', linewidth=2)
plt.grid(b=True, color='grey', alpha=0.1, linestyle='--', linewidth=1)
plt.show()