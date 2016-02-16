import pylab
import math
import scipy
import scipy.integrate

def dydt(y,t,g,l,q,Fd,w_d):
    theta = y[0]
    w = y[1]
    dtheta = w
    dw = -(g/l)*math.sin(theta) - q*dtheta + Fd*math.sin(w_d*t)
    return scipy.array([dtheta,dw])

def bifurcation():
    theta1 = 0.2 #theta in radians
    #theta1 = math.radians(theta1)
    w1 = 0
    l = 9.8
    g = 9.8
    dt = 0.01
    Fd = 1.35
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
