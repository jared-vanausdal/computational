import pylab
import scipy
import math
import scipy.integrate
from scipy import histogram

def dydt(y,t,g,l,q,Fd,w_d):
    theta = y[0]
    w = y[1]
    dtheta = w
    dw = -(g/l)*math.sin(theta) - q*dtheta + Fd*math.sin(w_d*t)
    return scipy.array([dtheta,dw])

def entropy():
    theta1 = 0.2 #theta in radians
    #theta1 = math.radians(theta1)
    w1 = 0
    l = 9.8
    g = 9.8
    dt = 0.01
    Fd = 1.3
    q = 0.5
    w_d = 2.0/3.0
    fd_list = []
    theta_list = []
    stepsize = ((2.0*math.pi)/w_d)
    time = 1000*stepsize
    t = scipy.arange(0,time,stepsize)
    y_init = scipy.array([theta1,w1])
    fd_valuelist = [Fd]
    S_list = [0]
    Pi_sum = 0
    while Fd < 1.49:
        print Fd
        y1 = scipy.integrate.odeint(dydt,y_init,t,args=(g,l,q,Fd,w_d))
        theta_final = y1[:,0]
        theta_final = abs(((theta_final + math.pi)%(2.0*math.pi)) - math.pi)
        theta_histval,binvals = scipy.histogram(theta_final,100,((-1)*math.pi,math.pi))
        prob_density = scipy.zeros(len(theta_histval))
        #print len(theta_histval)
        #print theta_histval
        for i in range(len(theta_histval)):
            prob_density[i] = float(theta_histval[i]) / len(theta_final)
            if prob_density[i] != 0:
                Pi_sum = Pi_sum + (prob_density[i]*math.log(prob_density[i]))
        print prob_density
        Pi_sum = Pi_sum * (-1)
        print Pi_sum
        S_list.append(Pi_sum)
        Pi_sum = 0
        Fd += 0.001
        fd_valuelist.append(Fd)
    pylab.scatter(fd_valuelist,S_list)
    pylab.xlabel('Driving Force')
    pylab.ylabel('Entropy')
    pylab.show()
    return 
