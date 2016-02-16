import scipy
import math
import pylab

def y_step(new,curr,prev,i):
    if i == (len(new)-1):
        new[i] = (curr[i-1]) - prev[i]
    elif i == 0:
        new[i] = (curr[i+1]) - prev[i]
    else:
        new[i] = (curr[i+1] + curr[i-1]) - prev[i]
    return new, curr, prev

def bookkeeping(new,curr,prev):
    prev = curr
    curr= new
    new = range(len(new))
    return curr, prev, new
    '''for i in range(len(new)):
        prev[i] = curr[i]
        curr[i] = new[i]
    new = zero_array(new)
    return curr, prev, new'''

def zero_array(array):
    for i in range(len(array)):
        array[i]=0
    return array


def init_pos(curr):
    L = len(curr)
    steps = L/2
    y_max = 0.02
    dy = 0.001
    dy2 = -0.002
    y1 = scipy.linspace(0,y_max,steps)
    y2 = scipy.linspace(y_max,0,steps)
    total_length = len(y1) + len(y2)
    y_array = scipy.concatenate((y1,y2),0)
    for i in range(len(curr)):
        curr[i] = y_array[i]
    return curr

def calculate(t,counter,new,curr,prev,x_array):
    while t <= 10:
        counter += 1
        for i in range(len(x_array)):
            new,curr,prev = y_step(new,curr,prev,i)
        curr, prev, new = bookkeeping(new,curr,prev)
        if counter == 10:
            #print(counter)
            pylab.plot(x_array,curr)
            counter = 0
        t += 0.1
    return
    
def plot(x,y):
    pylab.plot(x,y)

def main():
    L = 1
    n = 1000
    
    x_array = scipy.linspace(0,L,n)
    new = scipy.linspace(0,L,n)
    curr = scipy.linspace(0,L,n) #Creates 4 new arrays each of equal length
    prev = scipy.linspace(0,L,n)

    new= zero_array(new)
    curr = zero_array(curr) #Puts zeros in all of the array values
    prev = zero_array(prev)
    
    list1 = []
    counter = 0
    t = 0
    
    curr = init_pos(curr)
    prev = init_pos(prev)

    calculate(t,counter,new,curr,prev,x_array)
    pylab.show()
    return

