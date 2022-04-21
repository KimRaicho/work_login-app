# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# setting the x - coordinates
x1 = np.arange(0, 20 * np.pi, 0.1)
# setting the corresponding y - coordinates
y1 = np.sin(x1)

# plotting the points
plt.plot(x1, y1, label='ARM SIGNAL', linestyle='dashed')

x2 = np.arange(0, 20 * np.pi, 0.05)
# setting the corresponding y - coordinates
y2 = np.cos(x2)

# plotting the points
plt.plot(x2, y2, label='SPEED SIGNAL')

plt.ylabel('Amplitude')
plt.xlabel('Reflection Angles')

plt.xlim(0, 100)
plt.ylim(-1.5, 1.5)

plt.title('Signal to move Robotic Arms')

plt.legend(loc='upper right')

# function to show the plot
plt.show()






