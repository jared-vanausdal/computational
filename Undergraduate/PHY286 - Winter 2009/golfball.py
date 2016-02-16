import visual
import pylab
import math

def golfball_step(t,x,y,z,vx,vy,vz,m,g,B2,S0,w,dt,w_vector,v_vector):
    t = t+dt
    x = x + vx*dt
    y = y + vy*dt
    z = z + vz*dt
    FM = (S0*visual.cross(w_vector,v_vector))/m
    #vz = vz + (Fmz/m)*dt
    vz = vz + FM.z*dt#((S0*w*vx)*dt)
    v = math.sqrt((vx**2)+(vy**2)+(vz**2))
    vx = vx - (((B2*v*vx)/m)*dt) + FM.x*dt#((S0*w*vy)*dt)
    vy = vy - g*dt - (((B2*v*vy)/m)*dt) + FM.y*dt#((S0*w*vz)*dt)
    return t,x,y,z,vx,vy,vz

def golf_ball_calc(x,y,z,vx,vy,vz,dt,m,g,B2,S0,w,w_vector):
    t = 0.0
    x_list = [x]
    y_list = [y]
    z_list = [z]
    vx_list = [vx]
    vy_list = [vy]
    vz_list = [vz]
    t_list = [t]
    v_vector = visual.vector(vx,vy,vz)

    tee = visual.box(pos=(0,0,0), length=0.05, width=0.05, height=0.5,color=visual.color.white)
    ball = visual.sphere(pos=(x,y,z), radius = 0.25, color = visual.color.white)
    ball.trail = visual.curve(color = visual.color.red)

    while y > 0.0:
        visual.rate(100)
        t,x,y,z,vx,vy,vz = golfball_step(t,x,y,z,vx,vy,vz,m,g,B2,S0,w,dt,w_vector,v_vector)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        vx_list.append(vx)
        vy_list.append(vy)
        vz_list.append(vz)
        t_list.append(t)
        v_vector = visual.vector(vx,vy,vz)
        ball.pos = (x,y,z)
        ball.trail.append(pos=ball.pos)

    return t_list,x_list,y_list,z_list,vx_list,vy_list,vz_list

def run_golfball():
    v0 = 70 #initial velocity in m/s
    theta = 9 #launch angle in degrees
    m = 0.045 #mass of a golf ball in kg
    w = 2000/(2*math.pi)
    wx = w*math.cos(math.pi/4)
    wy = w*math.sin(math.pi/4)
    w_vector = visual.vector(wx,wy,0)
    B2 = m*4e-5
    S0 = m*4.1e-4
    g = 9.8
    dt = 0.001
    x = 0.0
    y = 0.5
    z = 0.0
    theta_radians = math.radians(theta)
    vx = v0*math.cos(theta_radians)
    vy = v0*math.sin(theta_radians)
    vz = 0
    t,x,y,z,vx,vy,vz = golf_ball_calc(x,y,z,vx,vy,vz,dt,m,g,B2,S0,w,w_vector)
    plot(x,y,z)

def plot(x,y,z):
    pylab.plot(x,y)
    pylab.plot(x,z)
    pylab.show()
