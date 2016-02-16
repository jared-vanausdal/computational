import pylab
import math
import visual

#Problem 2.13

def batted_ball_rangestep(x,y,vx,vy,dt):
    vd = 35
    g = 9.801
    d = 5
    x = x + (vx*dt)
    y = y + (vy*dt)
    v = math.sqrt((vx**2)+(vy**2))
    b = 0.0039 + (0.0058/(1+math.exp((v-vd)/d)))
    vx = vx - ((b*v*vx)*dt)
    vy = vy - ((g + (b*v*vy))*dt)
    return x,y,vx,vy

def batted_ball_range_nw():
    angle = 91
    x_max = 0
    max_angle = 0
    for i in range(angle):
        v = 49
        theta = math.radians(i)
        vx = v*math.cos(theta)
        vy = v*math.sin(theta)
        x = 0
        y = 1
        dt = 0.001
        x_list = [x]
        y_list = [y]
        while y >= 0:
            x,y,vx,vy = batted_ball_rangestep(x,y,vx,vy,dt)
            x_list.append(x)
            y_list.append(y)
        x_list.reverse()
        if x_list[0] > x_max:
            x_max = x_list[0]
            max_angle = i
    return max_angle,x_max

def batted_ball_rangestep_hw(x,y,vx,vy,dt):
    vd = 35
    vw = -11.18
    g = 9.801
    d = 5
    x = x + (vx*dt)
    y = y + (vy*dt)
    v = math.sqrt(((vx-vw)**2)+(vy**2))
    b = 0.0039 + (0.0058/(1+math.exp(((v-vw)-vd)/d)))
    vx = vx - ((b*v*vx)*dt)
    vy = vy - ((g + (b*v*vy))*dt)
    return x,y,vx,vy

def batted_ball_range_hw():
    angle = 91
    x_max = 0
    max_angle = 0
    for i in range(angle):
        v = 49
        theta = math.radians(i)
        vx = v*math.cos(theta)
        vy = v*math.sin(theta)
        x = 0
        y = 1
        dt = 0.001
        x_list = [x]
        y_list = [y]
        while y >= 0:
            x,y,vx,vy = batted_ball_rangestep_hw(x,y,vx,vy,dt)
            x_list.append(x)
            y_list.append(y)
        x_list.reverse()
        if x_list[0] > x_max:
            x_max = x_list[0]
            max_angle = i
    return max_angle,x_max

def batted_ball_rangestep_tw(x,y,vx,vy,dt):
    vd = 35
    vw = 11.18
    g = 9.801
    d = 5
    x = x + (vx*dt)
    y = y + (vy*dt)
    v = math.sqrt(((vx-vw)**2)+(vy**2))
    b = 0.0039 + (0.0058/(1+math.exp(((v-vw)-vd)/d)))
    vx = vx - ((b*v*vx)*dt)
    vy = vy - ((g + (b*v*vy))*dt)
    return x,y,vx,vy

def batted_ball_range_tw():
    angle = 91
    x_max = 0
    max_angle = 0
    for i in range(angle):
        v = 49
        theta = math.radians(i)
        vx = v*math.cos(theta)
        vy = v*math.sin(theta)
        x = 0
        y = 1
        dt = 0.001
        x_list = [x]
        y_list = [y]
        while y >= 0:
            x,y,vx,vy = batted_ball_rangestep_tw(x,y,vx,vy,dt)
            x_list.append(x)
            y_list.append(y)
        x_list.reverse()
        if x_list[0] > x_max:
            x_max = x_list[0]
            max_angle = i
    return max_angle,x_max

def run_battedball():
    print "No Wind Max Range(Angle, Range):", batted_ball_range_nw()
    print "Tail Wind Max Range(Angle, Range):", batted_ball_range_tw()
    print "Head Wind Max Range (Angle, Range):", batted_ball_range_hw()

    
#Problem 2.19


def spin_step(x,y,vx,vy,fm,dt):
    vd = 35
    g = ((6.67*(10**-11))*(5.9736*(10**24)))/(((6378.1*1000)+y)**2)
    d = 5
    x = x + (vx*dt)
    y = y + (vy*dt)
    v = math.sqrt((vx**2)+(vy**2))
    b = 0.0039 + (0.0058/(1+math.exp((v-vd)/d)))
    vx = vx - ((b*v*vx)*dt)
    vy = vy - ((g + (b*v*vy))*dt) + (fm*dt)
    return x,y,vx,vy,fm
    
def backspin():
    v = 49
    s0 = (4.1*(10**-4))
    w = ((2000*(2*math.pi))/60)
    theta = math.radians(35)
    vx = v*math.cos(theta)
    vy = v*math.sin(theta)
    fm = s0*w*vx
    x = 0
    y = 1
    dt = 0.001
    x_list = [x]
    y_list = [y]
    while y >= 0:
        x,y,vx,vy,fm = spin_step(x,y,vx,vy,fm,dt)
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list

def frontspin():
    v = 49
    s0 = (4.1*(10**-4))
    w = -((2000*(2*math.pi))/60)
    theta = math.radians(35)
    vx = v*math.cos(theta)
    vy = v*math.sin(theta)
    fm = s0*w*vx
    x = 0
    y = 1
    dt = 0.001
    x_list = [x]
    y_list = [y]
    while y >= 0:
        x,y,vx,vy,fm = spin_step(x,y,vx,vy,fm,dt)
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list

def batted_ball_rangestep2(x,y,vx,vy,dt):
    vd = 35
    g = ((6.67*(10**-11))*(5.9736*(10**24)))/(((6378.1*1000)+y)**2)
    d = 5
    x = x + (vx*dt)
    y = y + (vy*dt)
    v = math.sqrt((vx**2)+(vy**2))
    b = 0.0039 + (0.0058/(1+math.exp((v-vd)/d)))
    vx = vx - ((b*v*vx)*dt)
    vy = vy - ((g + (b*v*vy))*dt)
    return x,y,vx,vy

def batted_ball_range():
    v = 49
    theta = math.radians(35)
    vx = v*math.cos(theta)
    vy = v*math.sin(theta)
    vxh = vx
    vyh = vy
    vxt = vx
    vyt = vy
    x = 0
    y = 1
    dt = 0.001
    x_list = [x]
    y_list = [y]
    while y >= 0:
        x,y,vx,vy = batted_ball_rangestep2(x,y,vx,vy,dt)
        x_list.append(x)
        y_list.append(y)
    return x_list,y_list

def run_range():
    a,b = batted_ball_range()
    c,d = backspin()
    e,f = frontspin()
    pylab.plot(a,b,label="No Spin")
    pylab.plot(c,d,label="Backspin")
    pylab.plot(e,f,label="Topspin")
    pylab.legend()
    pylab.xlabel("Distance(m)")
    pylab.ylabel("Height(m)")
    pylab.title("Trajectory of Batted Ball")
    save = raw_input("Save file?(y,n):)
    if save == "y":
        filename = raw_input("Save file as:")
        pylab.savefig(filename,dpi=(640/8))
    pylab.show()

#Problem 2.25

def golfball_step(x,y,z,vx,vy,vz,g,S0,dt,w_vector,v_vector,ball):
    x = x + vx*dt
    y = y + vy*dt
    z = z + vz*dt
    FM = (S0*visual.cross(w_vector,v_vector))/ball.mass
    if v_vector.mag <= 14:
        ball.drag = 0.5*ball.airdensity*ball.area
    else:
        ball.C = 7.0/v_vector.mag
        ball.drag = ball.C*ball.airdensity*ball.area
    vz = vz - (((ball.drag*v_vector.mag*vz)/ball.mass)*dt)+ FM.z*dt
    v_vector = visual.vector(vx,vy,vz)
    v = v_vector.mag
    vx = vx - (((ball.drag*v*vx)/ball.mass)*dt) + FM.x*dt
    vy = vy - g*dt - (((ball.drag*v*vy)/ball.mass)*dt) + FM.y*dt
    return x,y,z,vx,vy,vz,ball

def golf_ball_calc(x,y,z,vx,vy,vz,dt,m,g,B2,S0,w_vector,v_vector,r,C,A):
    x_list = [x]
    y_list = [y]
    z_list = [z]
    vx_list = [vx]
    vy_list = [vy]
    vz_list = [vz]

    tee = visual.box(pos=(0,0,0), length=0.05, width=0.05, height=0.5,color=visual.color.white)
    ball = visual.sphere(pos=(x,y,z), radius = 0.25, color = visual.color.white)
    ball.trail = visual.curve(color = visual.color.red)
    ball.mass = m
    ball.drag = B2
    ball.area = A
    ball.C = C
    ball.airdensity = r

    while y > 0.0:
        #visual.rate(100)
        x,y,z,vx,vy,vz,ball = golfball_step(x,y,z,vx,vy,vz,g,S0,dt,w_vector,v_vector,ball)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        vx_list.append(vx)
        vy_list.append(vy)
        vz_list.append(vz)
        v_vector = visual.vector(vx,vy,vz)
        ball.pos = (x,y,z)
        ball.trail.append(pos=ball.pos)

    endpoint = visual.box(pos=(x,y,z), length=0.05,width=0.05,height=1.5,color=visual.color.white)
    flag = visual.pyramid(pos=(x,y+1.0,z),size=(3,1,0.05),color=visual.color.yellow)

    return x_list,y_list,z_list,vx_list,vy_list,vz_list

def run_golfball():
    v0 = 70 #initial velocity in m/s
    theta = 9 #launch angle in degrees
    m = 0.045 #mass of a golf ball in kg
    w = 5800/(2*math.pi)
    wz = w*math.cos(math.pi/4)
    wy = w*math.sin(math.pi/4)
    w_vector = visual.vector(0,wy,wz)
    r = 1.204
    C = 7.0/v0
    A = 0.00143
    B2 = C*r*A
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
    v_vector = visual.vector(vx,vy,vz)
    x,y,z,vx,vy,vz = golf_ball_calc(x,y,z,vx,vy,vz,dt,m,g,B2,S0,w_vector,v_vector,r,C,A)
    plot(x,y,z)

def plot(x,y,z):
    pylab.plot(x,y,label="Vertical Trajectory")
    pylab.plot(x,z,label="Horizontal Trajectory")
    pylab.legend(loc=8)
    save = raw_input("Save File?(y,n):")
    if save == "y":
        filename = raw_input("Save file as:")
        pylab.savefig(filename,dpi=(640/8))
    pylab.show()
