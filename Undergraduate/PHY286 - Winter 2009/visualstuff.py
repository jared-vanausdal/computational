import pylab
import visual
import math

def ball_step(x,y,z,vx,vy,vz,g,ball,S0,w_vector,dt):
    v_vector = visual.vector(vx,vy,vz) #Defines velocity vector based on components

    FM = S0 * visual.cross(w_vector,v_vector) / ball.mass #Finds acceleration from Magnus Force
    
    x = x + vx*dt
    y = y + vy*dt #Alters the position
    z = z + vz*dt

    vz = vz + FM.z*dt #Changes vz based on the Magnus acceleration in the Z direction
    
    v = v_vector.mag #defines v as the magnitude of the velocity vector for use below

    vx = vx - (((ball.drag*v*vx)/ball.mass)*dt) + FM.x*dt #updates x component of velocity
    
    vy = vy - 9.8*dt - (((ball.drag*v*vy)/ball.mass)*dt)# + FM.y*dt #updates y component of velocity
    '''This is where I believe my problem exists. I cannot figure out why the other two velocities are altered by the
    effect of the magnus force, but in this equation, y is not being altered at least noticeably.'''

    return x,y,z,vx,vy,vz

def ball_calc(x,y,z,vx,vy,vz,g,m,B2,S0,w_vector,dt):
    x_list = [x]
    y_list = [y]
    z_list = [z]

    tee = visual.box(pos = (0,0,0), length = 0.05, width = 0.05, height = 0.5, color = visual.color.white)
    ball = visual.sphere(pos = (0,0,0), radius = 0.05, color = visual.color.white)
    ball.trail = visual.curve(color = visual.color.red)
    ball.mass = m
    ball.drag = B2

    while y >= 0.0:
        visual.rate(100)
        x,y,z,vx,vy,vz = ball_step(x,y,z,vx,vy,vz,g,ball,S0,w_vector,dt)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        ball.pos = (x,y,z)
        ball.trail.append(pos = ball.pos)
    return x_list,y_list,z_list

def plot(x,y,z):
    pylab.plot(x,y)
    pylab.plot(x,z)
    pylab.show()

    
dt = 0.01
x = 0
y = 0
z = 0
v0 = 70 #initial velocity in m/s
theta = 9 #launch angle in degrees
theta_rad = math.radians(theta)
vx = v0*math.cos(theta_rad)
vy = v0*math.sin(theta_rad)
vz = 0
g = 9.8
m = 0.045
B2 = m*4e-5
S0 = m*4.1e-4              
w = (2000*(2*math.pi))/60
wx = w*math.cos(math.pi/4)
wy = w*math.sin(math.pi/4)
w_vector = visual.vector(wx,wy,0)
x,y,z = ball_calc(x,y,z,vx,vy,vz,g,m,B2,S0,w_vector,dt)
plot(x,y,z)
