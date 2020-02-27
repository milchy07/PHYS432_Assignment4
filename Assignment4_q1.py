import numpy as np
import matplotlib.pyplot as plt
import math
import pdb

#Question 1 -- Solving the Advection Equation

#Setting the constant variables
u = -0.1
t_step = 1
x_step = 1
grid_size = 100
steps = 1000

#Creating our array
grid = np.arange(grid_size)*x_step
temp = (u*t_step)/(2*x_step)

#FCTS initialization, normalized by grid size
f = np.copy(grid)*1.0/grid_size
#Lax-Friedrichs initialization, normalized by grid size
ff = np.copy(grid)*1.0/grid_size

#Initial plotting of state s/t it stays on plot the entire time
plt.ion()
fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True)
ax1 = axs[0]
ax2 = axs[1]
a1, = ax1.plot(grid,f,'bo')
a2, = ax2.plot(grid,ff,'ro')
#Defining the axes range
for ax in axs:
    ax.set_xlim([0,grid_size])
    ax.set_ylim([0,2])

ax1.set_title('FCTS')
ax2.set_title('Lax-Friedrichs')
ax1.set_xlabel('x')
ax2.set_xlabel('x')
ax1.set_ylabel('f(x,t)')
ax2.set_ylabel('f(x,t)')
fig.canvas.draw()
i = 0
#pdb.set_trace()
while i < steps:
    #FCTS
    f[1:grid_size-1] = f[1:grid_size-1] -temp*(f[2:]-f[:grid_size-2])
    #Lax-Friedrichs
    ff[1:grid_size-1] = 0.5*(ff[2:]+ff[:grid_size-2]) - temp*(ff[2:]-ff[:grid_size-2])
    #Plot updating
    a1.set_ydata(f)
    a2.set_ydata(ff)
    fig.canvas.draw()
    plt.pause(0.001)
    i = i + 1
