# Two plots with some customizations

import matplotlib.pyplot as plt

x1_values = [0, 2, 3, 4]
y1_values = [0, 1, 2, 4]
x2_values = [0, 1, 4, 6]
y2_values = [0, 1, 2, 1]

fig, ax = plt.subplots()

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.grid(visible=True, linestyle=":")

ax.plot(x1_values, y1_values, linestyle="--", color="red")
ax.plot(x2_values, y2_values, color="green")

fig.canvas.manager.set_window_title("Sample Figure")

plt.show()
