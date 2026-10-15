import numpy as np
import scipy.optimize as so
import matplotlib.pyplot as plt
import math


def y(x):
    return 5 * np.sin(5*x)

for i in range(-10,10):
    print(i)
    x0 = so.fsolve(y,i)
    print("Lsg ist ",x0)


x = np.linspace(-10,10,100000)
fig = plt.figure()
plt.plot(x,y(x))
plt.show()
