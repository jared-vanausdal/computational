import scipy
import pylab
import math


def psi_step(psi,E,i,dx,k):
    V = 0.5*(i**k)
    psi[i+1] = -2*(E-V)*psi[i]*(dx**2) + 2*psi[i] - psi[i-1]
    return psi

def main():
    E = .5
    for k in range(2,16):
        psi = scipy.zeros(100)
        psi = psi.tolist()
        psi[0]=1
        psi[1]=1
        for i in range(1,len(psi)-1):
            dx = 1.0/100
            psi = psi_step(psi,E,i,dx,k)
    x_array = range(0,20)
    psi = psi[:20]
    pylab.plot(x_array,psi)
    #pylab.ylim(-1,1)
    pylab.show()
