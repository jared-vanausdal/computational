def range_calc(v,theta):
    theta = math.radians(theta)
    vx = v*math.cos(theta)
    vy = v*math.sin(theta)
    x = 0
    y = 0
    dt = 0.001
    b = 4.e-5
    x_list = [x]
    y_list = [y]
    while y >= 0:
        x,y,vx,vy = range_step(x,y,vx,vy,b,dt)
        x_list.append(x)
        y_list.append(y)
    return x_list,y_list

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

def run_range():                    #Runs the range calculation with varying
    x,y = range_calc(500,55)        #launch angles
    a,b = range_calc(500,50)
    c,d = range_calc(500,45)
    e,f = range_calc(500,40)
    g,h = range_calc(500,35)
    pylab.plot(x,y)
    pylab.plot(a,b)
    pylab.plot(c,d)
    pylab.plot(e,f)
    pylab.plot(g,h)
    pylab.xlabel("Distance(m)")
    pylab.ylabel("Height(m)")
    pylab.title("Trajectory of a Cannonball")
    filename = raw_input("Save graph as:")
    pylab.savefig(filename,dpi=(640/8))
    pylab.show()
