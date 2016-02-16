import random
import scipy
import math
import pylab
from scipy import polyval, polyfit


def main():
    m = raw_input('Please enter number of walkers:')
    n = raw_input('Please enter number of steps:')

    m = int(m)
    n = int(n)
    x = scipy.zeros(m)
    y = scipy.zeros(m)
    z = scipy.zeros(m)
    r2 = scipy.zeros(m)

    r_sum = 0
    
    r2avg = scipy.zeros(n)
    t = scipy.arange(0,n,1)

    for i in range(n):
        for k in range(m):
            phi = random.uniform(0,(2*math.pi))
            theta = random.uniform(0,math.pi)
            x[k] = x[k] + (math.sin(theta)*math.cos(phi))
            y[k] = y[k] + (math.sin(theta)*math.sin(phi))
            z[k] = z[k] + (math.cos(theta))
            r2[k] = ((x[k])**2) + ((y[k])**2) + ((z[k])**2)
            r_sum = r_sum + r2[k]

        r2avg[i] = r_sum / m
        r_sum = 0

    (ar,br)=polyfit(t,r2avg,1) 
    r_regression = polyval([ar,br],t) #Linear Regression


    pylab.scatter(t,r2avg,label='R2 Average(%.2f walker(s))'%(m))
    pylab.plot(t,r_regression,label='Linear Regression y=%.2f*t'%(ar))
    pylab.legend(loc=4)
    pylab.xlabel('Time(steps)')
    pylab.ylabel('<r2>')
    #pylab.savefig('R2_image6.png',dpi=(640/8))
    pylab.show()
    return     
            
