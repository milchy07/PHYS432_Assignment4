import numpy as np
import matplotlib.pyplot as plt
import math

#Question 2 -- Solving the Advection-Diffusion Equation

#Setting the constant variables
u = -0.1
t_step = 1
x_step = 1
grid_size = 100
steps = 1000
D1 = 0.1
D2 = 1
beta1 = (D1*t_step)/(x_step**2)
beta2 = (D2*t_step)/(x_step**2)

#Creating our array
grid = np.arange(grid_size)*x_step
temp = (u*t_step)/(2*x_step)

#Lax-Friedrichs initialization
f = np.copy(grid)
ff = np.copy(grid)
#Initial plotting of state s/t it stays on plot the entire time
plt.ion()
fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True)
ax1 = axs[0]
ax2 = axs[1]
a1, = ax1.plot(grid,f,'bo')
a2, = ax2.plot(grid,ff,'ro')
ax1.set_title('Lax-Friedrichs, D = 0.1')
ax2.set_title('Lax-Friedrichs, D = 1')
ax1.set_xlabel('x')
ax2.set_xlabel('x')
ax1.set_ylabel('f(x,t)')
ax2.set_ylabel('f(x,t)')
fig.canvas.draw()
i = 0
while i < steps:
    #Solving diffusion part
    A1 = np.eye(grid_size)*(1+2*beta1) - beta1*np.eye(grid_size,k=1) -beta1*np.eye(grid_size,k=-1)
    print(len(A1))
    #BCs
    A1[0][0] = 1
    A1[0][1] = 0
    A1[-1][-1] = 1
    A1[-1][-2] = 0

    A2 = np.eye(grid_size)*(1+2*beta2) - beta2*np.eye(grid_size,k=1) -beta2*np.eye(grid_size,k=-1)
    #BCs
    A2[0][0] = 1
    A2[0][1] = 0
    A2[-1][-1] = 1
    A2[-1][-2] = 0
    #Diffusion terms
    f = np.linalg.solve(A1,f)
    ff = np.linalg.solve(A2,ff)
    #Advection terms
    f[1:grid_size-1] = 0.5*(f[2:]+f[:grid_size-2]) - temp*(f[2:]-f[:grid_size-2])
    ff[1:grid_size-1] = 0.5*(ff[2:]+ff[:grid_size-2]) - temp*(ff[2:]-ff[:grid_size-2])
    #Plot updating
    a1.set_ydata(f)
    a2.set_ydata(ff)
    fig.canvas.draw()
    plt.pause(0.00001)
    i = i + 1
