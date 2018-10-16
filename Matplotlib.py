import matplotlib.pylab as plt
import numpy as np

v = 25  # Velocity
g = 9.8  # Gravity
theta = np.arange(np.pi/3) # Angle

plt.figure()

tmax = ((2*v)*np.sin(theta))/g   # Formula to find time
timemat = tmax*np.linspace(start = 0, stop = 1)[:, None]  # Time vector

x = ((v*timemat)*np.cos(theta))  # Formula to find the x position
y = ((v*timemat)*np.sin(theta)) - (0.5*g)*(timemat**2)  # Formula to find y position

plt.plot(x,y)
plt.ylim([0,35])
plt.show()