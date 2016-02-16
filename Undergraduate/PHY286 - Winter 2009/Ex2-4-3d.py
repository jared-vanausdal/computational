# Program to calculate the trajectory of a baseball including air resistance and spin.
import visual
import pylab
import math


def do_time_step(t, dt, x, y, z, vx, vy, vz, m, B2, g, S0, omega):
    """ Update the position and velocity components of the baseball. """
    t = t + dt
    x = x + vx*dt
    y = y + vy*dt
    z = z + vz*dt

    vz = vz - S0*vx*omega/m*dt # update vz first to use current value of vx
    v = math.sqrt(vx*vx + vy*vy + vz*vz)
    vx = vx - B2/m*v*vx*dt
    vy = vy - g*dt - B2/m*v*vy*dt

    return t, x, y, z, vx, vy, vz

def calculate(x, y, z, vx, vy, vz, dt, m, g, B2, S0, omega):
    """ Calculate the trajectory of a baseball including air resistance and spin by
repeatedly calling the do_time_step function.  Also draw the trajectory using visual python. """
    t = 0.0
    # Establish lists with initial position and velocity components and time.
    x_list = [x]
    y_list = [y]
    z_list = [z]
    vx_list = [vx]
    vy_list = [vy]
    vz_list = [vz]
    t_list = [t]

    # Set up visual elements.
    mound = visual.box(pos=(0,0,0), length=0.1, width=0.5, height=0.03, color=visual.color.white)
    plate = visual.box(pos=(18,0,0), length=0.5, width=0.5, height=0.03, color=visual.color.white)
    ball = visual.sphere(pos=(x,y,z), radius=0.05, color=visual.color.white)
    ball.trail = visual.curve(color=ball.color)

    while y >= 0.0:
        visual.rate(100) # Limit to no more than 100 iterations per second.
        t, x, y, z, vx, vy, vz = do_time_step(t, dt, x, y, z, vx, vy, vz, m, B2, g, S0, omega)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        vx_list.append(vx)
        vy_list.append(vy)
        vz_list.append(vz)
        t_list.append(t)
        ball.pos = (x,y,z)
        ball.trail.append(pos=ball.pos)

    return t_list, x_list, y_list, z_list, vx_list, vy_list, vz_list

def interpolate(x_list, y_list, z_list):
    """Do a linear interpolation to find landing point of the baseball."""
    x1 = x_list[-2]
    x2 = x_list[-1]
    y1 = y_list[-2]
    y2 = y_list[-1]
    z1 = z_list[-2]
    z2 = z_list[-1]
    r = -y1/y2
    x_land = (x1+r*x2)/(r+1)
    z_land = (z1+r*z2)/(r+1)
    x_list[-1] = x_land
    y_list[-1] = 0.0
    z_list[-1] = z_land
    

def output(t, x, y, z, vx, vy, vz):
    """ Output results to a file. """
    f = open('baseball.out', 'w')
    for i in range(len(t)):
        f.write(str(t[i])+', '+str(x[i])+', '+str(y[i])+', '+str(z[i])+','+str(vx[i])+', '+str(vy[i])+', '+str(vz[i])+'\n')
    f.close()
    
def plot(x, y, z):
    """ Plot y versus x and z versus x. """
    pylab.plot(x, y)
    pylab.plot(x, z)
    pylab.show()

v0 = 31 # Initial speed in m/s
theta = 2 # Initial angle of pitch in degrees
omega = 2*math.pi*30 # Angular velocity in radians per second
m = 0.149 # mass of baseball in kilograms
B2 = m*4e-5 # drag coefficient in kg/m
S0 = m*4.1e-4 # Magnus coefficient in kg
g = 9.8 # acceleration of gravity in m/s^2
dt = 0.001 # delta t in seconds

x = 0.0 # Initial x position (toward home plate) in meters
y = 2 # Initial height of ball in meters
z = 0.0 # Initial z position (toward third base) of ball in meters
theta_rad = math.radians(theta)
vx = v0*math.cos(theta_rad)
vy = v0*math.sin(theta_rad)
vz = 0
t, x, y, z, vx, vy, vz = calculate(x, y, z, vx, vy, vz, dt, m, g, B2, S0, omega)
#interpolate(x, y, z)
plot(x,y,z)
output(t, x, y, z, vx, vy, vz)
