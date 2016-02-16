import pylab
import math

#Problem 2.3
def v_step(v, t, P, m, dt):
    t = t + dt
    v = v + (P/(m*v))*dt
    return t, v

def v_airstep(v,P,m,C,A,r,dt):
    v = v + (P/(m*v))*dt - ((C*r*A*(v**2))/(2*m))*dt
    return v

def v_viscstep(v,P,m,C,A,n,h,r,dt):
    v = v + (P/(m*v))*dt - ((C*r*A*(v**2))/(2*m))*dt - ((n*A*(v/h))/m)*dt
    return v
    

def v_calc(v, t_final, P, m, C, A, n, h, r, dt):
    t = 0
    i = 0
    t_list = [t]
    v_list = [v]
    v_air = [v]
    va = v
    vv = v
    v_visc = [v]
    while i < t_final:
        t,v = v_step(v,t,P,m,dt)
        va = v_airstep(va,P,m,C,A,r,dt)
        vv = v_viscstep(vv,P,m,C,A,n,h,r,dt)
        t_list.append(t)
        v_list.append(v)
        v_air.append(va)
        v_visc.append(vv)
        i = i + dt
    return t_list, v_list, v_air, v_visc

def plot(x,y,z,a):
    pylab.plot(x,y,label='No Air Resistance')
    pylab.plot(x,z,label='Air Resistance')
    pylab.plot(x,a,label='Viscous Drag')
    pylab.xlabel("Time(seconds)")
    pylab.ylabel("Velocity(m/s)")
    pylab.title("Velocity vs. Time")
    pylab.legend(loc=2)
    filename = raw_input("Save output as:")
    pylab.savefig(filename,dpi=(640/8))
    pylab.show()

def run_velocity():
    C = 0.5
    A = 0.33
    n = 1.e-3 #Changed this value between 1.e-3 and 2.e-5 for water vs air
    r = 1.241
    t,v,vair,vvisc = v_calc(4,100,400,70,C,A,n,1.5,r,0.1)
    plot(t,v,vair,vvisc)


#Problem 2.8

def range_calc(v,theta):
    theta = math.radians(theta)
    vx = v*math.cos(theta)
    vy = v*math.sin(theta)
    x = 0
    y = 0
    a = x
    c = y
    d = vx
    e = vy
    f = x
    g = y
    h = vx
    i = vy
    j = x
    k = y
    l = vx
    m = vy
    dt = 0.001
    b = 4.e-5
    x_list = [x]
    y_list = [y]
    ideal_x = [x]
    ideal_y = [y]
    gravity_x = [x]
    gravity_y = [y]
    density_x = [x]
    density_y = [y]
    while y >= 0:
        x,y,vx,vy = range_step(x,y,vx,vy,b,dt)
        x_list.append(x)
        y_list.append(y)
    while c >= 0:
        a,c,d,e = range_stepideal(a,c,d,e,dt)
        ideal_x.append(a)
        ideal_y.append(c)
    while g >= 0:
        f,g,h,i = range_stepgravity(f,g,h,i,dt)
        gravity_x.append(f)
        gravity_y.append(g)
    while k >= 0:
        j,k,l,m = range_constantdensity(j,k,l,m,b,dt)
        density_x.append(j)
        density_y.append(k)
    return x_list,y_list,ideal_x,ideal_y,gravity_x,gravity_y,density_x,density_y

def range_step(x,y,vx,vy,b,dt):
    g = ((6.67*(10**-11))*(5.9736*(10**24)))/(((6378.1*1000)+y)**2)
    x = x + vx*dt
    y = y + vy*dt
    r0 = 1.204
    r = r0*(((1-(((6.5*(10**-3))*y)/293.15)))**2.5)
    b2 = b * (r/r0)
    v = math.sqrt((vx**2)+(vy**2))
    vx = vx - ((b2*v*vx)*dt)
    vy = vy - ((g+(b2*v*vy))*dt)
    return x,y,vx,vy

def range_stepideal(x,y,vx,vy,dt):
    g = 9.8
    x = x + vx*dt
    y = y + vy*dt
    vx = vx
    vy = vy - ((g)*dt)
    return x,y,vx,vy

def range_stepgravity(x,y,vx,vy,dt):
    g = ((6.67*(10**-11))*(5.9736*(10**24)))/(((6378.1*1000)+y)**2)
    x = x + vx*dt
    y = y + vy*dt
    vx = vx
    vy = vy - ((g)*dt)
    return x,y,vx,vy

def range_constantdensity(x,y,vx,vy,b,dt):
    g = ((6.67*(10**-11))*(5.9736*(10**24)))/(((6378.1*1000)+y)**2)
    x = x + vx*dt
    y = y + vy*dt
    v = math.sqrt((vx**2)+(vy**2))
    vx = vx - ((b*v*vx)*dt)
    vy = vy - ((g+(b*v*vy))*dt)
    return x,y,vx,vy

def run_range():                                #Runs the range calculation with varying
    x,y,t,v,r,s,q,p = range_calc(500,55)        #launch angles
    a,b,t,v,r,s,q,p = range_calc(500,50)        #t,v,r,s,q,p are dummy variables to 
    c,d,t,v,r,s,q,p = range_calc(500,45)        #not cause errors, not used in this function
    e,f,t,v,r,s,q,p = range_calc(500,40)
    g,h,t,v,r,s,q,p = range_calc(500,35)
    pylab.plot(x,y,label="55")
    pylab.plot(a,b,label="50")
    pylab.plot(c,d,label="45")
    pylab.plot(e,f,label="40")
    pylab.plot(g,h,label="35")
    pylab.xlabel("Distance(m)")
    pylab.ylabel("Height(m)")
    pylab.title("Trajectory of a Cannonball")
    pylab.legend(loc=8,title="Firing Angle")
    filename = raw_input("Save graph as:")
    pylab.savefig(filename,dpi=(640/8))
    pylab.show()

def compare_range():
    a,b,c,d,e,f,g,h = range_calc(500,45)
    pylab.plot(a,b,label="Real Range")
    pylab.plot(c,d,label="Ideal Range")
    pylab.plot(e,f,label="Variable Gravity")
    pylab.plot(g,h,label="Constant Density")
    pylab.xlabel("Distance(m)")
    pylab.ylabel("Height(m)")
    pylab.title("Realistic Trajectory vs. Ideal Trajectory")
    pylab.legend(loc=0)
    filename = raw_input("Save graph as:")
    pylab.savefig(filename,dpi=(640/8))
    pylab.show()
