# Program to calculate the oscillation of a small amplitude pendulum.
from __future__ import division
import pylab
import math
import scipy
import scipy.integrate



def dydt(y, t, g, L):
    theta = y[0]
    omega = y[1]
    dtheta = omega
    domega = -g/L*theta
    return scipy.array([dtheta, domega])


def output(t, x, y):
    f = open('pendulum-euler.out', 'w')
    for i in range(len(t)):
        f.write(str(t[i])+', '+str(x[i])+', '+str(y[i])+'\n')
    f.close()
    
def plot(x, y):
    pylab.plot(x, y)
    pylab.show()

theta_deg = 3 # Initial angle of pendulum in degrees
theta = math.radians(theta_deg)
omega = 0
L = 1 # length of pendulum
g = 9.8 # acceleration of gravity in m/s^2
time = 10 # total time of calculation in s
dt = 0.01
nsteps = int(time/dt)

t = scipy.linspace(0, time, nsteps)
y0 = scipy.array([theta, omega])
y = scipy.integrate.odeint(dydt, y0, t, args=(g, L))
theta = y[:,0]
omega = y[:,1]
plot(t, theta)
output(t, theta, omega)
