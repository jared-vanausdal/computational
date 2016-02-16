import pylab
import math
import numpy

#Problem 3.2

def pendulum_step(theta1, w1, t, dt):
    w = w1 - ((9.8/1)*theta1*dt)
    theta = theta1 + w1*dt
    t = t + dt
    return theta, w, t

def pendulum_calc():
    t = 0
    m = 1
    theta = 10
    theta = math.radians(theta)
    w = 0
    dt = 0.001
    E = 0.5*m*((w**2)+(9.8*(theta**2)))
    t_list = [t]
    theta_list = [theta]
    E_list = [E]
    while t <= 100:
        theta,w,t = pendulum_step(theta,w,t,dt)
        E = (0.5)*m*((w**2)+(9.8*(theta**2)))
        t_list.append(t)
        theta_list.append(theta)
        E_list.append(E)
    return t_list,theta_list,E_list

def RK_pendulum():
    t = 0
    m = 1
    theta = 10
    theta = math.radians(theta)
    w = 0
    E = 0.5*m*((w**2)+(9.8*(theta**2)))
    dt = 0.001
    t_list=[t]
    theta_list=[theta]
    E_list=[E]
    while t <= 100:
        theta,w,t = RK_pendulum_step(theta,w,t,dt)
        E = 0.5*m*((w**2)+(9.8*(theta**2)))
        t_list.append(t)
        theta_list.append(theta)
        E_list.append(E)
    return t_list,theta_list,E_list

def RK_pendulum_step(theta0,w0,t,dt):
    t = t + dt
    w1 = w0 - (9.8*theta0*(0.5*dt))
    theta1 = theta0 + (w0*(0.5*dt))    
    w_final = w0 - (9.8*theta1*dt)
    theta_final = theta0 + (w1*dt)
    return theta_final,w_final,t

def compare_plot(t1,theta1,e1,t2,theta2,e2):
    #pylab.plot(t1,theta1,label='Euler')
    pylab.plot(t1,e1,label='Euler Energy')
    #pylab.plot(t2,theta2,label='RK')
    pylab.plot(t2,e2,label='RK Energy')
    pylab.xlabel('Time(s)')
    pylab.ylabel('Energy(J)')
    pylab.legend()
    pylab.ylim(0,0.5)
    #filename = raw_input('Save figure as:')
    #pylab.savefig(filename,dpi=(640/8))
    pylab.show()
'''
t1,theta1,e1 = pendulum_calc()
t2,theta2,e2 = RK_pendulum()
compare_plot(t1,theta1,e1,t2,theta2,e2)'''

#Problem 3.8
def RK_largeangle(theta):
    t = 0
    m = 1
    thetarad = math.radians(theta)
    w = 0
    dt = 0.001
    t_list=[t]
    theta_list=[theta]
    while t <= 10:
        thetarad,w,t = RK_largeangle_step(thetarad,w,t,dt)
        t_list.append(t)
        theta = math.degrees(thetarad)
        theta_list.append(theta)
    return t_list,theta_list

def RK_largeangle_step(theta0,w0,t,dt):
    t = t + dt
    w1 = w0 - (9.8*(math.sin(theta0))*(0.5*dt))
    theta1 = theta0 + (w0*(0.5*dt))    
    w_final = w0 - (9.8*(math.sin(theta1))*dt)
    theta_final = theta0 + (w1*dt)
    return theta_final,w_final,t

def T_compare(t1,theta1,t2,theta2,t3,theta3,t4,theta4):
    pylab.plot(t1,theta1,label='165 Degrees')
    pylab.plot(t2,theta2,label='125 Degrees')
    pylab.plot(t3,theta3,label='90 Degrees')
    pylab.plot(t4,theta4,label='45 Degrees')
    pylab.legend()
    pylab.xlabel('Time(s)')
    pylab.ylabel('Theta(Degrees)')
    pylab.title('Theta vs. Time')
    #filename = raw_input('Save file as:')
    #pylab.savefig(filename,dpi=(640/8))
    pylab.show()
    
'''
theta_init1 = 165
theta_init2 = 125
theta_init3 = 90
theta_init4 = 45
t1,theta1 = RK_largeangle(theta_init1)
t2,theta2 = RK_largeangle(theta_init2)
t3,theta3 = RK_largeangle(theta_init3)
t4,theta4 = RK_largeangle(theta_init4)
T_compare(t1,theta1,t2,theta2,t3,theta3,t4,theta4)'''

#Problem 3.11

def RK_driven(Fd):
    t = 0
    m = 1
    theta = 0.2
    w = 0
    g = 9.8
    l = 9.8
    q = 0.5
    w_d = 2.0/3.0
    E = 0.5*m*(l**2)*(w**2) + m*g*l*(1-math.cos(theta))
    dt = 0.04
    t_list=[t]
    theta_list=[theta]
    E_list=[E]
    while t <= 50:
        theta,w,t = RK_driven_step(theta,w,t,dt,q,g,l,Fd,w_d)
        E = 0.5*m*(l**2)*(w**2) + m*g*l*(1-math.cos(theta))
        E_list.append(E)
        t_list.append(t)
        theta_list.append(theta)
    return t_list,theta_list,E_list

def RK_driven_step(theta0,w0,t0,dt,q,g,l,Fd,w_d):
    t1 = t0 + 0.5*dt
    t = t0 + dt
    w1 = w0 - (((g/l)*math.sin(theta0)*(dt/2)) + ((q*w0)*(dt/2)) - ((Fd*math.sin(w_d*t0)*(dt/2))))
    theta1 = theta0 + (w0*(0.5*dt))
    w_final = w0 - (((g/l)*math.sin(theta1)*(dt)) + ((q*w1)*(dt)) - (Fd*math.sin(w_d*t1)*(dt)))
    theta_final = theta0 + (w1*dt)
    return theta_final,w_final,t

'''
t1,theta1,e1 = RK_driven(0)
t2,theta2,e2 = RK_driven(0.6)
t3,theta3,e3 = RK_driven(1.2)
#pylab.plot(t1,theta1,label='Fd = 0')
pylab.plot(t1,e1,label='Fd = 0 Energy')
#pylab.plot(t2,theta2,label='Fd = 0.6')
pylab.plot(t2,e2,label='Fd = 0.6 Energy')
#pylab.plot(t3,theta3,label='Fd = 1.2')
pylab.plot(t3,e3,label='Fd = 1.2 Energy')
pylab.title('Energy vs. Time')
pylab.xlabel('Time(s)')
pylab.ylabel('Energy(J)')
pylab.legend()
filename = raw_input('Save file as:')
pylab.savefig(filename,dpi=(640/8))
pylab.show()'''


#Trapezoid Method
def trap(f,a,b,n):
    dt = float (abs(b-a))/n
    area = (dt*0.5)*(f(a)+f(b)+ (2*sum(f(a+i*dt) for i in range(1,n))))
    return area

def f(x):
    return 2.0*x


#Simpson Method
def simpson(f,a,b,n):
    dt = float (abs(b-a))/n
    area = (dt/3.0)*(f(a)+f(b)+sum((2*(i%2+1))*f(a+i*dt) for i in range(1,n)))
    return area

#Romberg Integration

def romberg(f,a,b,err):
    i = 0
    newrow = []
    '''if i < 2:
        Rerr = abs(0-(trap(f,a,b,1)))
    else:
        Rerr = abs(newrow[i-2] - newrow[i-1])'''
    while test_error(newrow,i) > err:
        oldrow = newrow
        newrow = []
        i += 1
        for j in range(i):
            newrow.append(0)
        newrow[0] = trap(f,a,b,i)
        for j in range(1,i):
            newrow[j] = newrow[j-1] + ((newrow[j-1] - oldrow[j-1]) / (4**(j) - 1))
    return newrow[i-1]


def test_error(newrow,i):
    if i < 2:
        Rerr = 100#abs(0-(trap(f,a,b,i)))
    else:
        Rerr = abs(newrow[i-2] - newrow[i-1])
    return Rerr
