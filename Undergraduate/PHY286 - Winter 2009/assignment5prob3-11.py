import pylab
import math

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
    dt = 0.04
    t_list=[t]
    theta_list=[theta]
    while t <= 60:
        theta,w,t = RK_driven_step(theta,w,t,dt,q,g,l,Fd,w_d)
        t_list.append(t)
        theta_list.append(theta)
    return t_list,theta_list

def RK_driven_step(theta0,w0,t0,dt,q,g,l,Fd,w_d):
    t1 = t0 + 0.5*dt
    t = t0 + dt
    w1 = w0 - (((g/l)*math.sin(theta0)*(dt/2)) + ((q*w0)*(dt/2)) - ((Fd*math.sin(w_d*t0)*(dt/2))))
    theta1 = theta0 + (w0*(0.5*dt))
    w_final = w0 - (((g/l)*math.sin(theta1)*(dt)) + ((q*w1)*(dt)) - (Fd*math.sin(w_d*t1)*(dt)))
    theta_final = theta0 + (w1*dt)
    return theta_final,w_final,t

t1,theta1 = RK_driven(0)
t2,theta2 = RK_driven(0.5)
t3,theta3 = RK_driven(1.2)
pylab.plot(t1,theta1,label='Fd = 0')
pylab.plot(t2,theta2,label='Fd = 0.5')
pylab.plot(t3,theta3,label='Fd = 1.2')
pylab.legend()
pylab.show()

