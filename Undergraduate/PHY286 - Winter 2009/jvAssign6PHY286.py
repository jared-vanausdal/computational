import pylab
import math
import scipy
import scipy.integrate



#Problem 3.12
def poincare():
    theta1 = 0.2 #theta in radians
    theta2 = 0.2
    theta3 = 0.2
    #theta1 = math.radians(theta1)
    #theta2 = math.radians(theta2)
    w1 = 0
    w2 = 0
    w3 = 0
    l = 9.8
    g = 9.8
    dt = 0.04
    Fd = 1.2
    q = 0.5
    w_d = 2.0/3.0
    stepsize = (2.0*math.pi/w_d)
    time = stepsize*1000
    
    t1 = scipy.arange(0,time,stepsize)
    t2 = scipy.arange((math.pi/4),time+(math.pi/4),stepsize)
    t3 = scipy.arange((math.pi/2),time+(math.pi/4),stepsize)
    y1_init = scipy.array([theta1,w1])
    y1 = scipy.integrate.odeint(dydt,y1_init,t1,args=(g,l,q,Fd,w_d))
    y2_init = scipy.array([theta2,w2])
    y2 = scipy.integrate.odeint(dydt,y2_init,t2,args=(g,l,q,Fd,w_d))
    y3_init = scipy.array([theta3,w3])
    y3 = scipy.integrate.odeint(dydt,y3_init,t3,args=(g,l,q,Fd,w_d))
    
    theta1 = y1[1:,0]
    theta1 = ((theta1 + math.pi)%(2.0*math.pi)) - math.pi
    w1 = y1[1:,1]

    theta2 = y2[1:,0]
    theta2 = ((theta2 + math.pi)%(2.0*math.pi)) - math.pi
    w2 = y2[1:,1]

    theta3 = y3[1:,0]
    theta3 = ((theta3 + math.pi)%(2.0*math.pi)) - math.pi
    w3 = y3[1:,1]
    
    poincare_plot(theta1,w1,theta2,w2,theta3,w3)

def poincare_plot(x,y,u,v,t,z):
    pylab.scatter(x,y,label='In Phase')
    pylab.scatter(u,v,label='Pi/4 Out of Phase', c='red')
    pylab.scatter(t,z,label='Pi/2 Out of Phase', c='black')
    pylab.xlabel('Theta(Radians)')
    pylab.ylabel('Omega(Rads/s)')
    pylab.title('W vs. Theta')
    pylab.legend()
    pylab.show()


#Problem 3.13
def dydt(y,t,g,l,q,Fd,w_d):
    theta = y[0]
    w = y[1]
    dtheta = w
    dw = -(g/l)*math.sin(theta) - q*dtheta + Fd*math.sin(w_d*t)
    return scipy.array([dtheta,dw])

def plot(x,y,z):
    pylab.plot(x,y,label='3 Degrees')
    pylab.plot(x,z,label='4 Degrees')
    pylab.legend()
    pylab.xlabel('Time(s)')
    pylab.ylabel('Theta(Radians)')
    pylab.title('Theta vs. Time')
    pylab.show()

def deltaplot(x,y):
    pylab.semilogy(x,y)
    pylab.xlabel('Time(s)')
    pylab.ylabel('Delta Theta(Radians) Log-scale')
    pylab.show()


def chaotic():
    theta1 = 0.200 #theta in radians
    theta2 = 0.201
    #theta1 = math.radians(theta1)
    #theta2 = math.radians(theta2)
    w1 = 0
    w2 = 0
    l = 9.8
    g = 9.8
    dt = 0.04
    time = 150
    Fd = 1.2
    q = 0.5
    w_d = 2.0/3.0
    steps = int(time/dt)
    
    t = scipy.linspace(0,time,steps)
    y1_init = scipy.array([theta1,w1])
    y1 = scipy.integrate.odeint(dydt,y1_init,t,args=(g,l,q,Fd,w_d))
    y2_init = scipy.array([theta2,w2])
    y2 = scipy.integrate.odeint(dydt,y2_init,t,args=(g,l,q,Fd,w_d))
    theta1 = y1[:,0]
    theta1 = ((theta1 + math.pi)%(2.0*math.pi)) - math.pi
    w1 = y1[:,1]
    theta2 = y2[:,0]
    theta2 = ((theta2 + math.pi)%(2.0*math.pi)) - math.pi
    w2 = y2[:,1]
    deltatheta = abs(theta1-theta2)
    #deltatheta = scipy.log(deltatheta)
    deltaplot(t,deltatheta)
    
#Problem 3.20


def bifurcation():
    theta1 = 0.2 #theta in radians
    #theta1 = math.radians(theta1)
    w1 = 0
    l = 9.8
    g = 9.8
    dt = 0.01
    Fd = 1.476
    q = 0.5
    w_d = 2.0/3.0
    fd_list = []
    theta_list = []
    stepsize = ((2.0*math.pi)/w_d)
    time = 450*stepsize
    t = scipy.arange(0,time,stepsize)
    y_init = scipy.array([theta1,w1])
    fd_valuelist = [Fd]
    while Fd < 1.5:
        y1 = scipy.integrate.odeint(dydt,y_init,t,args=(g,l,q,Fd,w_d))
        theta_final = y1[300:,0]
        theta_final = abs(((theta_final + math.pi)%(2.0*math.pi)) - math.pi)
        for i in range(100):
            fd_list.append(Fd)
            theta_list.append(theta_final[i])
        Fd += 0.001
        fd_valuelist.append(Fd)
    dn_list = []
    '''for n in range(len(fd_valuelist)):
        if n == 0:
            dn = fd_valuelist[n] / (fd_valuelist[n+1] - fd_valuelist[n])
            dn_list.append(dn)
        elif n == len(fd_valuelist):
            dn = (fd_valuelist[n]-fd_valuelist[n-1]) / (0 - fd_valuelist[n])
        else:
            dn = (fd_valuelist[n]-fd_valuelist[n-1]) / (fd_valuelist[n+1] - fd_valuelist[n])
            dn_list.append(dn)'''
    
    plot_bifurcation(fd_list,theta_list)
    return 

def plot_bifurcation(x,y):
    pylab.scatter(x,y)
    pylab.xlabel('Fd')
    pylab.ylabel('Theta(Radians)')
    pylab.show()
