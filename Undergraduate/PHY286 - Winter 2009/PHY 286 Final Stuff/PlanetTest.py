import math
import pylab
import scipy
import scipy.integrate
import visual

def dpos(x,t,g,m_s,m_e,m_j):
    e_x = x[0]
    e_y = x[1]

    s_x = x[2]
    s_y = x[3]

    j_x = x[4]
    j_y = x[5]

    e_vx = x[6]
    e_vy = x[7]

    s_vx = x[8]
    s_vy = x[9]

    j_vx = x[10]
    j_vy = x[11]

    e_dx = e_vx
    e_dy = e_vy

    s_dx = s_vx
    s_dy = s_vy

    j_dx = j_vx
    j_dy = j_vy

    r_ej = math.sqrt((j_x - e_x)**2 + (j_y - e_y)**2) #Finds the distance between each of the three bodies in 
    r_es = math.sqrt((e_x - s_x)**2 + (e_y - s_y)**2) #the Earth-Sun-Jupiter system
    r_sj = math.sqrt((j_x - s_x)**2 + (j_y - s_y)**2)

    e_dvx = -(g*m_s*(e_x - s_x)/(r_es**3)) - (g*m_j*(e_x - j_x)/(r_ej**3)) #The force on Earth is split between Jupiter
    e_dvy = -(g*m_s*(e_y - s_y)/(r_es**3)) - (g*m_j*(e_y - j_y)/(r_ej**3)) #and the sun, so the signs are opposite

    s_dvx = -(g*m_e*(s_x - e_x)/(r_es**3)) - (g*m_j*(s_x - j_x)/(r_sj**3)) #The Force on the sun and jupiter are the 
    s_dvy = -(g*m_e*(s_y - e_y)/(r_es**3)) - (g*m_j*(s_y - j_y)/(r_sj**3)) #same signs in this point of the orbits

    j_dvx = -(g*m_s*(j_x - s_x)/(r_sj**3)) - (g*m_e*(j_x - e_x)/(r_ej**3))
    j_dvy = -(g*m_s*(j_y - s_y)/(r_sj**3)) - (g*m_e*(j_y - e_y)/(r_ej**3))

##    #Determines where the bodies are in their orbit based on the distance between the Earth and Jupiter
##    #and adjusts the forces based on that determination
##    if r_sj >= r_ej:
##        e_dvx = -(g*m_s*(e_x - s_x)/(r_es**3)) + (g*m_j*(e_x - j_x)/(r_ej**3)) #The force on Earth is split between Jupiter
##        e_dvy = -(g*m_s*(e_y - s_y)/(r_es**3)) + (g*m_j*(e_y - j_y)/(r_ej**3)) #and the sun, so the signs are opposite
##
##        s_dvx = -(g*m_e*(s_x - e_x)/(r_es**3)) - (g*m_j*(s_x - j_x)/(r_sj**3)) #The Force on the sun and jupiter are the 
##        s_dvy = -(g*m_e*(s_y - e_y)/(r_es**3)) - (g*m_j*(s_y - j_y)/(r_sj**3)) #same signs in this point of the orbits
##
##        j_dvx = -(g*m_s*(j_x - s_x)/(r_sj**3)) - (g*m_e*(j_x - e_x)/(r_ej**3))
##        j_dvy = -(g*m_s*(j_y - s_y)/(r_sj**3)) - (g*m_e*(j_y - e_y)/(r_ej**3))
##    else:
##        e_dvx = -(g*m_s*(e_x - s_x)/(r_es**3)) - (g*m_j*(e_x - j_x)/(r_ej**3)) #Earth is no longer between the Sun and Jupiter
##        e_dvy = -(g*m_s*(e_y - s_y)/(r_es**3)) - (g*m_j*(e_y - j_y)/(r_ej**3)) #and so the signs of the forces are the same
##
##        s_dvx = -(g*m_e*(s_x - e_x)/(r_es**3)) + (g*m_j*(s_x - j_x)/(r_sj**3)) #The Sun is between Jupiter and Earth and so
##        s_dvy = -(g*m_e*(s_y - e_y)/(r_es**3)) + (g*m_j*(s_y - j_y)/(r_sj**3)) #the signs of the forces are opposite
##
##        j_dvx = -(g*m_s*(j_x - s_x)/(r_sj**3)) - (g*m_e*(j_x - e_x)/(r_ej**3))
##        j_dvy = -(g*m_s*(j_y - s_y)/(r_sj**3)) - (g*m_e*(j_y - e_y)/(r_ej**3))

    return scipy.array([e_dx,e_dy,s_dx,s_dy,j_dx,j_dy,e_dvx,e_dvy,s_dvx,s_dvy,j_dvx,j_dvy])

def main():
    g = 1.186*(10**-4) #Gravitational constant in AU^3 / (Earth Mass * year^2)

    m_s = 332900 #Mass of Sun in Earth masses
    m_e = 1
    #m_j = 318 #Mass of Jupiter in Earth masses
    #m_j = 5*318 #Sets mass of Jupiter as 5 times its normal mass
    m_j = 100*318 #Sets mass of Jupiter as 100 times its normal mass
    #m_j = 1e3*318 #Sets mass of Jupiter as 1000 times its normal mass

    e_x0 = 0.983289 #Starting point is perihelion of Earth
    e_y0 = 0
    e_vx = 0
    e_vy = 6.2819373 #Velocity of Earth in AU/year

    j_x0 = 4.950429 #Starting point is perihelion of Jupiter
    j_y0 = 0
    j_vx = 0
    j_vy = 2.75704904 #Velocity of Jupiter in AU/year

    s_x0 = -4.73181e-3 #Starting point of the sun to make the center of mass the origin
    s_y0 = 0
    s_vx = 0              #The starting velocity of the Sun is set relative to 
    #s_vy = -0.0026521887  #the other bodies in this system so that the total
    #s_vy = -0.0131871130 #momentum is 0
    s_vy = -0.263383723
    #s_vy = -2.63366740
    
    t = scipy.arange(0,5,0.01)
    x0 = scipy.array([e_x0,e_y0,s_x0,s_y0,j_x0,j_y0,e_vx,e_vy,s_vx,s_vy,j_vx,j_vy])

    x = scipy.integrate.odeint(dpos,x0,t,args=(g,m_s,m_e,m_j),rtol = 1e-6)

    e_x = x[:,0]
    e_y = x[:,1]

    s_x = x[:,2]
    s_y = x[:,3]

    j_x = x[:,4]
    j_y = x[:,5]

    #Creates the visual python elements

##    earth = visual.sphere(pos=(e_x0,e_y0),radius=4.25e-8,color=visual.color.blue)
##    earth.trail = visual.curve(color = visual.color.blue)
##
##    jupiter = visual.sphere(pos=(j_x0,j_y0),radius=0.000478,color=visual.color.red)
##    jupiter.trail = visual.curve(color = visual.color.red)
##
##    sun = visual.sphere(pos=(s_x0,s_y0),radius=0.004646,color=visual.color.orange)
##    sun.trail = visual.curve(color = visual.color.orange)
##
##    #Creates the orbits of the bodies
##    for i in range(len(e_x)):
##        x,y = e_x[i],e_y[i]
##        earth.pos =(x,y)
##        earth.trail.append(pos=earth.pos)
##
##        x,y = s_x[i],s_y[i]
##        sun.pos = (x,y)
##        sun.trail.append(pos=sun.pos)
##
##        x,y = j_x[i],j_y[i]
##        jupiter.pos = (x,y)
##        jupiter.trail.append(pos=jupiter.pos)

    #Creates a graph of the orbits of the bodies
    pylab.plot(e_x,e_y,label='Earth')
    pylab.plot(j_x,j_y,label='Jupiter')
    pylab.plot(s_x,s_y,label='Sun')
    pylab.xlabel('x position (AUs)')
    pylab.ylabel('y position (AUs)')
    pylab.title('Orbit of Sun-Earth-Jupiter System')
    pylab.legend()
    pylab.show()

main()
