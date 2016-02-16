import pylab
import math
import scipy

def psi_function(length, iseven, E, n, dx):
    psi = scipy.arange(0,length,dx)
    psi[0],psi[1] = init_conditions(iseven)
    for i in range(2,len(psi)):
        psi[i] = calc_psi(E,V(n,i*dx),dx,psi,i)
    return psi

def calc_psi(e,v,dx,psi,i):
    psi[i] = -2.0*(e-v)*psi[i-1]*(dx**2) + 2.0*psi[i-1] - psi[i-2]
    return psi[i]

def V(n,x):
    v = 0.5*(x**n)
    return v

def init_conditions(iseven):
    if iseven == True:
        return 1,1
    else:
        return 0,1

def find_length(E,n):
    x = 2.0*((2.0*E)**(1.0/n))
    return x;

def psi_test(l,iseven,E,n,dx,dE,r,prev_E):
    condition = False
    e_high = False
    e_low = False
    tol = 0.001
    counter = 0
    psi = psi_function(l,iseven,E,n,dx)
    while condition != True:
        psi = psi_function(l,iseven,E,n,dx)
        if r <= 1:
            if psi[len(psi)-1] > tol and E >= prev_E:
                e_high = True
                E = E + dE
                if e_low == True and e_high == True:
                    dE = dE/2.0
                    e_low = False
                    e_high = False
                counter +=1
    #            print e_low, e_high, counter, E
            elif psi[len(psi)-1] < ((-1)*tol) and E >= prev_E:
                e_low = True
                E = E - dE
                if e_low == True and e_high == True:
                    dE = dE/2.0
                    e_low = False
                    e_high = False
                counter += 1
     #           print e_low, e_high, counter, E
            else:
                condition = True
        else:
            if psi[len(psi)-1] > tol:
                e_high = True
                E = E - dE
                if e_low == True and e_high == True and E > prev_E:
                    dE = dE/2.0
                    e_low = False
                    e_high = False
                counter +=1
                #print e_low,e_high, counter, E
            elif psi[len(psi)-1] < ((-1)*tol):
                e_low = True
                E = E + dE
                if e_low == True and e_high == True and E > prev_E:
                    dE = dE/2.0
                    e_low = False
                    e_high = False
                counter += 1
                #print e_low, e_high, counter, E
            else:
                condition = True
    return psi,E

def output(n,e_list):
    print 'n=%.2f : '%(n)
    print '1st Stable Energy %.2f'%(e_list[0])
    print '2nd Stable Energy %.2f'%(e_list[1])
    print '3rd Stable Energy %.2f'%(e_list[2])
    print '4th Stable Energy %.2f'%(e_list[3])
    

def main():
    dE = 0.001
##    n = raw_input('Enter a value for n:')
##    E = raw_input('Enter an initial Energy value:')
    E = 0.5
    E1_list = []
    E2_list = []
    E3_list = []
    E4_list = []
##    n = int(n)
    for k in range(4):
        if k == 0:
            iseven = True
            n = 2
            prev_E = 0
#            print prev_E
            for r in range(4):
                if r == 3:
                    return 0.0
                else:
                    L = find_length(E,n)
                    dx = L/1000.0
                    psi,E = psi_test(L,iseven,E,n,dx,dE,r,prev_E)
                    E1_list.append(E)
                    prev_E = E
    #                print E
                    E += 0.01
    #                print E
                    if iseven == True:
                        iseven = False
                    else: iseven = True
                E = 0.5
                prev_E = 0
##        elif k == 1:
##            iseven = True
##            n = 4
##            prev_E = 0
##            #print prev_E
##            for r in range(4):
##                L = find_length(E,n)
##                dx = L/1000.0
##                psi,E = psi_test(L,iseven,E,n,dx,dE,r)
##                E2_list.append(E)
##                prev_E = E
##                #print prev_E
##                E+= 1
##                #print E
##                if iseven == True:
##                    iseven = False
##                else: iseven = True
##            E = 0.5
##            prev_E = 0
##        elif k == 2:
##            iseven = True
##            n = 8
##            prev_E = 0
##            #print prev_E
##            for r in range(4):
##                L = find_length(E,n)
##                dx = L/1000.0
##                psi,E = psi_test(L,iseven,E,n,dx,dE,r)
##                E3_list.append(E)
##                prev_E = E
##                #print prev_E
##                E += 1
##                #print E
##                if iseven == True:
##                    iseven = False
##                else: iseven = True
##            E = 0.5
##            prev_E = 0
##        else:
##            iseven = True
##            n = 16
##            prev_E = 0
##            for r in range(4):
##                L = find_length(E,n)
##                dx = L/1000.0
##                psi,E = psi_test(L,iseven,E,n,dx,dE,r)
##                prev_E = E
##                E4_list.append(E)
##                E += 1
##                if iseven == True:
##                    iseven = False
##                else: iseven = True
##            E = 0.5
##            prev_E = 0
        if k == 0:
            output(n,E1_list)
##        elif k == 1:
##            output(n,E2_list)
##        elif k == 2:
##            output(n,E3_list)
##        else:
##            output(n,E4_list)
