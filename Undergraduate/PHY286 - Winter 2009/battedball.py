import pylab
import math

def backspin_step(x,y,vx,vy,fm,dt):
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
    w = 33.3
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
        x,y,vx,vy,fm = backspin_step(x,y,vx,vy,fm,dt)
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list

def batted_ball_rangestep(x,y,vx,vy,dt):
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

def headwind_step(x,y,vx,vy,dt):
    vd = 35
    vw = 4.5
    g = ((6.67*(10**-11))*(5.9736*(10**24)))/(((6378.1*1000)+y)**2)
    d = 5
    x = x + (vx*dt)
    y = y + (vy*dt)
    v = math.sqrt((vx**2)+(vy**2))
    b = 0.0039 + (0.0058/(1+math.exp(((v-vw)-vd)/d)))
    vx = vx - ((b*v*vx)*dt)
    vy = vy - ((g + (b*v*vy))*dt)
    return x,y,vx,vy

def tailwind_step(x,y,vx,vy,dt):
    vd = 35
    vw = 4.5
    g = ((6.67*(10**-11))*(5.9736*(10**24)))/(((6378.1*1000)+y)**2)
    d = 5
    x = x + (vx*dt)
    y = y + (vy*dt)
    v = math.sqrt((vx**2)+(vy**2))
    b = 0.0039 + (0.0058/(1+math.exp(((v+vw)-vd)/d)))
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
    a = x
    b = y
    c = x
    d = y
    dt = 0.001
    x_list = [x]
    y_list = [y]
    headwind_xlist = [x]
    headwind_ylist = [y]
    tailwind_xlist = [x]
    tailwind_ylist = [y]
    while y >= 0:
        x,y,vx,vy = batted_ball_rangestep(x,y,vx,vy,dt)
        x_list.append(x)
        y_list.append(y)
    while b >= 0:
        a,b,vxh,vyh = headwind_step(a,b,vxh,vyh,dt)
        headwind_xlist.append(a)
        headwind_ylist.append(b)
    while d >= 0:
        c,d,vxt,vyt = tailwind_step(c,d,vxt,vyt,dt)
        tailwind_xlist.append(c)
        tailwind_ylist.append(d)
    return x_list, y_list,headwind_xlist,headwind_ylist,tailwind_xlist,tailwind_ylist

def plot(a,b,c,d,e,f,x,y):
    pylab.plot(a,b,label="No Wind")
    pylab.plot(c,d,label="Headwind")
    pylab.plot(e,f,label="Tailwind")
    pylab.plot(x,y,label="Backspin")
    pylab.title("Trajectory of Batted Baseball")
    pylab.xlabel("Distance(m)")
    pylab.ylabel("Height(m)")
    pylab.legend(loc=8)
    filename = raw_input("Save file as:")
    pylab.savefig(filename,dpi=(640/8))
    pylab.show()

a,b,c,d,e,f = batted_ball_range()
x,y = backspin()
plot(a,b,c,d,e,f,x,y)
