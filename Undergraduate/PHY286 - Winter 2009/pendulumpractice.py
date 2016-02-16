import math
import pylab
import visual

#Pendulum work. Chapter 3.

def pendulum_step(theta, w1, t, dt,E):
    E = E + (0.5*1*(w1**2+(9.8*(theta**2))))*(dt**2)
    w = w1 - ((9.8/1)*theta*dt)
    theta = theta + w1*dt
    t = t + dt
    return theta, w, t, E

def pendulum_calc():
    t = 0
    theta = 45
    theta = math.radians(theta)
    w = 0
    dt = 0.04
    E = (1-math.cos(theta))*9.8
    t_list = [t]
    theta_list = [theta]
    E_list = [E]
    while t <= 10:
        theta,w,t,E = pendulum_step(theta,w,t,dt,E)
        t_list.append(t)
        theta_list.append(theta)
        E_list.append(E)
    return t_list,theta_list,E_list

def plot(x,y):
    pylab.plot(x,y)
    pylab.show()

#theta,t = pendulum_calc()
#plot(t,theta)

#Pendulum. Euler-Cromer method.

def pendulum_cromer_step(theta,w,t,dt):
    w = w - (9.8*theta*dt)
    theta = theta + w*dt
    t = t + dt
    return theta, w, t

def pendulum_cromer():
    t = 0
    theta = 45
    theta = math.radians(theta)
    w = 0
    dt = 0.04
    t_list = [t]
    theta_list = [theta]
    while t <=10:
        theta,w,t = pendulum_cromer_step(theta,w,t,dt)
        t_list.append(t)
        theta_list.append(theta)
    return theta_list, t_list

#Pendulum Chapter. Ex. 3.1

def E_pendulum_cromer_step(theta,w,t,dt,E,m):
    #E = E + ((0.5*m*9.8*(w**2+(9.8*theta**2)))*(dt**2))
    w = w - (9.8*theta*dt)
    theta = theta + w*dt
    E = E + ((0.5*m*(w**2+(9.8*theta**2)))*(dt**2))
    t = t + dt
    return theta, w, t, E

def E_pendulum_cromer():
    t = 0
    m = 1
    theta = 10
    theta = math.radians(theta)
    E = (1-math.cos(theta))*9.8*m #initial E is only potential at starting point of pendulum
    w = 0
    dt = 0.04
    t_list = [t]
    theta_list = [theta]
    E_list = [E]
    while t <=10:
        theta,w,t,E = E_pendulum_cromer_step(theta,w,t,dt,E,m)
        t_list.append(t)
        theta_list.append(theta)
        E_list.append(E)
    return theta_list, t_list, E_list

def plot_three(x,y,z):
    pylab.plot(x,y)
    pylab.plot(x,z)
    pylab.show()

def RK_pendulum():
    t = 0
    m = 1
    theta = 10
    theta = math.radians(theta)
    E = (1-math.cos(theta))*9.8*m
    w0 = 0
    dt = 0.04
    t_list=[t]
    theta_list=[theta]
    E_list=[E]
    while t <= 10:
        theta,w,t,E = RK_pendulum_step(theta,w0,t,dt,E)
        t_list.append(t)
        theta_list.append(theta)
        E_list.append(E)
    return t_list,theta_list,E_list

def RK_pendulum_step(theta0,w0,t,dt,E):
    t = t + dt
    w1 = w0 - (9.8*theta0*(0.5*dt))
    theta1 = theta0 + (w0*(0.5*dt))    
    w_final = w0 - (9.8*theta1*dt)
    theta_final = theta0 + (w1*dt)
    E = E + ((0.5*1*(w_final**2+(9.8*(theta_final**2))))*(dt**2))
    return theta_final,w_final,t,E

def plot_six(x1,y1,z1,x2,y2,z2):
    pylab.plot(x1,y1)
    pylab.plot(x1,z1)
    pylab.plot(x2,y2)
    pylab.plot(x2,z2)
    pylab.show()

t1,theta1,e1 = pendulum_calc()
t2,theta2,e2 = RK_pendulum()
plot_three(t2,theta2,e2)
#plot_six(t1,theta1,e1,t2,theta2,e2)
