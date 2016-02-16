import pylab

def calculate(E, V_n, dx, phin, phin1):
    return -2*(E-V_n)*phin*(dx)**2 + 2*phin - phin1


def initials(even):
    if even == True:
        return 1, 1
    else: return 0, 1

def murder(length, even, E, nexp, dx):
    y = range(length)
    y[0], y[1] = initials(even)
    #y[1] = calculate(E, V(nexp, 1*dx), dx, 1, 1)
    for i in range(2, length):
        y[i] = calculate(E, V(nexp, i*dx), dx, y[i-1], y[i-2])
    return y

def V(nexp, x):
    return 0.5*x**nexp

def findoverlap(E, nexp, dx):
    i = 2
    while E >= V(nexp, i*dx):
        i += 1
    return i

def findE(tol, start, initialChange, even, nexp, dx):
    Ehigh, Elow = -1, -1
    E = start
    while Ehigh < 0 or Elow < 0:
        Ecurr = findPoint(even, E, nexp, dx)
        if abs(Ecurr) < tol:
            return E
        elif Ecurr < 0:
            Ehigh = E
        else:
            Elow = E
        E += initialChange
    passes = 0
    maxpasses = 300
    while abs(Ecurr) > tol and passes < maxpasses:
        passes += 1
        E = (Ehigh + Elow)/2
        Ecurr = findPoint(even, E, nexp, dx)
        if Ecurr < 0:
            Ehigh = E
        else: Elow = E
    if passes >= maxpasses:
        print "pass limit reached, Ecurr, E, Ehigh/low", Ecurr, E, (Ehigh, Elow)
    return E

def findPoint(even, E, nexp, dx):
    length = findoverlap(E, nexp, dx)
    length *= 6
    x = murder(length, even, E, nexp, dx)
    return x[-1]

def plot(y, dx, overlap):
    x = range(len(y))
    for i in x:
        x[i] *= dx
    pylab.plot(x, y)
    pylab.scatter(overlap*dx, y[overlap])
    pylab.scatter(overlap*dx, 0)

dx = 0.001
nexp = 2
even = True
E = findE(0.1, .6, 0.2, even, nexp, dx)
print E
#E = 2.50211623027
overlap = findoverlap(E, nexp, dx)
length = int(overlap*4)
y = murder(length, even, E, nexp, dx)

plot(y, dx, overlap)
idk = y[:overlap]
maxx = max(idk) * 1.1
minn = min(idk) * 1.1
if abs(minn) > abs(maxx):
    maxx = abs(minn)
pylab.ylim(-maxx, maxx)

pylab.show()
