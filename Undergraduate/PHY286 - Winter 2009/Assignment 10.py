#Assignment 10
from __future__ import division
import pylab
import math
import numpy
import scipy

E=7.14/2
steps=100
even=1
n=2

def calc(E,steps,n,iseven):
    dx=.1
    iseven = iseven % 2
    L=2*(2*E)**(1/n)
    x=scipy.linspace(0,L,steps)
    new=scipy.zeros(steps)
    if iseven == 0:
        new[0] = 1
    else:
        new[0]=0
    new[1] = 1
    for i in range(2,steps):
        V=.5*(x[i])**n
        new[i] = (-1)*(E-V)*(new[i-1])*((dx)**2) + 2*(new[i-1]) - (new[i-2])
    return new,x

def main(E,steps,n):
    last_div = 0
    stepnumber = 1
    new,x = calc(E,steps,n,stepnumber)
    if new[len(new)-1] > 

new,x=main(E,steps,n)

def plot (x,y):
    pylab.plot(x,y)
    pylab.show()

plot(x,new)
