import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(xlim=(-10, 10),ylim=(0,100))
x, y = [], []
line, = plt.plot([], [],'ro',markersize=3)


def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = np.linspace(-10,-10+frame)
    y= x**2
    #y = np.sin( np.pi * (x + 0.02 * frame))
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=20,
                    init_func=init,interval=200)

ax.set_aspect(1./ax.get_data_ratio())
plt.grid()
plt.show()