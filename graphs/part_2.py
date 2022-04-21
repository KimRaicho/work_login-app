import matplotlib.pyplot as plt
import numpy as np

# part 2 analysis

# setting the x - coordinates
x3 = np.arange(0, 15 * np.pi, 0.2)
# setting the corresponding y - coordinates
y2 = np.cos(x3)
y3 = np.tan(x3)

# plotting the points
plt.plot(x3, y3, label='FAST SIGNAL')

plt.show()
