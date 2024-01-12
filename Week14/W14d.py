# Bar plot, custom colors

import matplotlib.pyplot as plt

x_values = ["A", "B", "C", "D"]
y_values = [5, 7, 6, 8]
colors = ["red", "green", "blue", "orange"]

fig, ax = plt.subplots()
# ax.bar(x_values, y_values, color="green")
ax.bar(x_values, y_values, color=colors)

ax.set_title("Some Figure")
ax.set_xlabel("Letters")
ax.set_ylabel("Numbers")

plt.show()
