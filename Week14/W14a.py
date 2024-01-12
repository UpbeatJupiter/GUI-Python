# Simple plot

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4]
y_values = [5, 7, 6, 8]

fig, ax = plt.subplots()

ax.plot(x_values, y_values)

plt.show()
