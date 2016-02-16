import pylab
import math
import scipy
import scipy.integrate
import visual

def dposition(x,t,big_g,m_sun,m_earth,m_jupiter):
    e_x = x[0]
    e_y = x[1]
    e_z = x[2]

    s_x = x[3]
    s_y = x[4]
    s_z = x[5]

    j_x = x[6]
    j_y = x[7]
    j_z = x[8]

    e_vx = x[9]
    e_vy = x[10]
    e_vz = x[11]

    s_vx = x[12]
    s_vy = x[13]
    s_vz = x[14]

    j_vx = x[15]
    j_vy = x[16]
    j_vz = x[17]

    e_dx = e_vx
    e_dy = e_vy
    e_dz = e_vz

    s_dx = s_vx
    s_dy = s_vy
    s_dz = s_vz

    j_dx = j_vx
    j_dy = j_vy
    j_dz = j_vz

    
    r_es = math.sqrt((e_x-s_x)**2 + (e_y-s_y)**2 + (e_z-s_z)**2)
    r_ej = math.sqrt((e_x-j_x)**2 + (e_y-j_y)**2 + (e_z-j_z)**2)
    r_sj = math.sqrt((s_x-j_x)**2 + (s_y-j_y)**2 + (s_z-j_z)**2)

    if r_sj >= r_ej:
        e_dvx = -((big_g*(m_sun*e_x)/(r_es**3)) - (big_g*(m_jupiter*(e_x-j_x))/(r_ej**3)))
        e_dvy = -((big_g*(m_sun*e_y)/(r_es**3)) - (big_g*(m_jupiter*(e_y-j_y))/(r_ej**3)))
        e_dvz = -((big_g*(m_sun*e_z)/(r_es**3)) - (big_g*(m_jupiter*(e_z-j_z))/(r_ej**3)))
    
        s_dvx = -((big_g*(m_earth*s_x)/(r_es**3)) + (big_g*(m_jupiter*(s_x-j_x))/(r_sj**3)))
        s_dvy = -((big_g*(m_earth*s_y)/(r_es**3)) + (big_g*(m_jupiter*(s_y-j_y))/(r_sj**3)))
        s_dvz = -((big_g*(m_earth*s_z)/(r_es**3)) + (big_g*(m_jupiter*(s_z-j_z))/(r_sj**3)))

        j_dvx = -((big_g*(m_sun*j_x)/(r_sj**3)) + (big_g*(m_earth*(j_x-e_x))/(r_ej**3)))
        j_dvy = -((big_g*(m_sun*j_y)/(r_sj**3)) + (big_g*(m_earth*(j_y-e_y))/(r_ej**3)))
        j_dvz = -((big_g*(m_sun*j_z)/(r_sj**3)) + (big_g*(m_earth*(j_z-e_z))/(r_ej**3)))
    else:
        e_dvx = -((big_g*(m_sun*e_x)/(r_es**3)) + (big_g*(m_jupiter*(e_x-j_x))/(r_ej**3)))
        e_dvy = -((big_g*(m_sun*e_y)/(r_es**3)) + (big_g*(m_jupiter*(e_y-j_y))/(r_ej**3)))
        e_dvz = -((big_g*(m_sun*e_z)/(r_es**3)) + (big_g*(m_jupiter*(e_z-j_z))/(r_ej**3)))
    
        s_dvx = -((big_g*(m_earth*s_x)/(r_es**3)) - (big_g*(m_jupiter*(s_x-j_x))/(r_sj**3)))
        s_dvy = -((big_g*(m_earth*s_y)/(r_es**3)) - (big_g*(m_jupiter*(s_y-j_y))/(r_sj**3)))
        s_dvz = -((big_g*(m_earth*s_z)/(r_es**3)) - (big_g*(m_jupiter*(s_z-j_z))/(r_sj**3)))

        j_dvx = -((big_g*(m_sun*j_x)/(r_sj**3)) + (big_g*(m_earth*(j_x-e_x))/(r_ej**3)))
        j_dvy = -((big_g*(m_sun*j_y)/(r_sj**3)) + (big_g*(m_earth*(j_y-e_y))/(r_ej**3)))
        j_dvz = -((big_g*(m_sun*j_z)/(r_sj**3)) + (big_g*(m_earth*(j_z-e_z))/(r_ej**3)))
    
    return scipy.array([e_dx,e_dy,e_dz,s_dx,s_dy,s_dz,j_dx,j_dy,j_dz,e_dvx,e_dvy,e_dvz,s_dvx,s_dvy,s_dvz,j_dvx,j_dvy,j_dvz])

    

def calculate_motion():
    big_g = 1.186*(10**-4) #Gravitational Constant in AU^3/(Earth Mass)*(year^2)
    
    m_sun = 332900
    m_earth = 1
    m_jupiter = 5*318#*(1e3)#318
                
    e_posx = 0.983289 #Starting point is perihelion of Earth
    e_posy = 0
    e_posz = 0
    e_velx = 0
    e_vely = 6.2819373
    e_velz = 0

    j_posx = 4.950429 #Starting point is perihelion of Jupiter
    j_posy = 0
    j_posz = 0
    j_velx = 0#2.75
    j_vely = 2.75704904
    j_velz = 0

    s_posx = 0#-4.97026e-3
    s_posy = 0
    s_posz = 0
    s_velx = 0#3.14*(2*(-4.97e-3))#1e-8
    s_vely = 3.14*(2*(-4.97e-3))#1e-8
    s_velz = 0#3.14*(2*(-4.97e-3))#1e-8

    t = scipy.arange(0,1000,1e-3)
    planetary_init = scipy.array([e_posx,e_posy,e_posz,s_posx,s_posy,s_posz,j_posx,j_posy,j_posz,e_velx,e_vely,e_velz,s_velx,s_vely,s_velz,j_velx,j_vely,j_velz])
    
    planetary_motion = scipy.integrate.odeint(dposition,planetary_init,t,args=(big_g,m_sun,m_earth,m_jupiter),rtol=1e-6,atol=1e-6)#,full_output=1)

    e_x = planetary_motion[:,0]
    e_y = planetary_motion[:,1]
    e_z = planetary_motion[:,2]
    s_x = planetary_motion[:,3]
    s_y = planetary_motion[:,4]
    s_z = planetary_motion[:,5]
    j_x = planetary_motion[:,6]
    j_y = planetary_motion[:,7]
    j_z = planetary_motion[:,8]

##    earth = visual.sphere(pos=(e_posx,e_posy,e_posz),radius=4.25e-8,color=visual.color.blue)
##    earth.trail = visual.curve(color = visual.color.blue)
##
##    jupiter = visual.sphere(pos=(j_posx,j_posy,j_posz),radius=0.000478,color=visual.color.red)
##    jupiter.trail = visual.curve(color = visual.color.red)
##
##    sun = visual.sphere(pos=(s_posx,s_posy,s_posz),radius=0.004646,color=visual.color.orange)
##    sun.trail = visual.curve(color = visual.color.orange)
##
##    for i in range(len(e_x)):
##        x,y,z = e_x[i],e_y[i],e_z[i]
##        earth.pos =(x,y,z)
##        earth.trail.append(pos=earth.pos)
##
##        x,y,z = s_x[i],s_y[i],s_z[i]
##        sun.pos = (x,y,z)
##        sun.trail.append(pos=sun.pos)
##
##        x,y,z = j_x[i],j_y[i],j_z[i]
##        jupiter.pos = (x,y,z)
##        jupiter.trail.append(pos=jupiter.pos)
##        
        
    pylab.plot(e_x,e_y,'b',label='Earth')
##    pylab.plot(e_x,e_z,label='earth z')
    pylab.plot(s_x,s_y,'r',label='Sun')
    pylab.plot(j_x,j_y,'g',label='Jupiter')
    pylab.xlabel('X Distance(AUs)')
    pylab.ylabel('Y Distance(AUs)')
##    pylab.xlim(-15,15)
##    pylab.ylim(-15,15)
    pylab.legend()
    pylab.show()
    return

calculate_motion()
