from __future__ import division
import math, pylab

class Draw:
    counter = 0
    maxcounter = 1
    maxpsi = 0
    def __init__(self, mcount = 1):
        self.maxcounter = mcount
        #pylab.ion()
    
    def draw(self, psi, forceDraw = False, clear = False):
        if forceDraw == True:
            self._draw(psi, clear)
            return
        self.counter += 1
        if self.counter == self.maxcounter:
            self.counter = 0
            self._draw(psi, clear)
            
    def _draw(self, psi, clear):
        if clear == True:
            pylab.clf()
            self.maxpsi = 0
        pylab.plot(psi)
        length = int(len(psi)/6)
        idk = psi[:length]
        maxx = max(idk) * 1.1
        minn = min(idk) * 1.1
        if abs(minn) > abs(maxx):
            maxx = abs(minn)
        if maxx > self.maxpsi:
            self.maxpsi = maxx
        pylab.ylim(-self.maxpsi, self.maxpsi)
        #pylab.draw()

def oddeveninit(even):
    if even:
        return 1, 1
    else: return 0, 1/100

def V(nexp, x):
    return (x**nexp)/2

def findoverlap(E, nexp, dx):
    i = 0
    while E > V(nexp, i*dx):
        i += 1
    return i

def zero(E, v, dx, psia, psib):
    return 2*psia - psib - 2*(E-v)*psia*dx**2

def one(E, nexp, even, numi, dx, draw):
    psi = range(numi)
    psi[0], psi[1] = oddeveninit(even)
    i = 2
    while i < numi:
        psi[i] = zero(E, V(nexp, i*dx), dx, psi[i-1], psi[i-2])
        i += 1
    if draw != None:
        draw.draw(psi)
    return psi

def two(E, nexp, even, dx, extra, draw):
    overlap = findoverlap(E, nexp, dx)
    length = int(overlap * extra)
    psi = one(E, nexp, even, length, dx, draw)
    return psi
    
def quickDraw(ea, eva, nexp, dx, extra, draw):
    for i in range(len(ea)):
        psi = two(ea[i], nexp, eva[i], dx, extra, None)
        draw.draw(psi, True)

def lastpsi(psi, index = -1):
    lastPsi = psi[-1]
    if math.isnan(lastPsi) == True:
        i = 1
        while math.isnan(lastPsi) == True:
            lastPsi = psi[-i]
            i += 1
    return lastPsi

def three(E, etol, nexp, even, dx, extra, draw):
    #purpose: find a good e (energy) after the certain point
    eHighFound, eLowFound = False, False
    eHigh, eLow = 0, 0
    eCurr = E
    someE = 0.1
    while not eHighFound or not eLowFound:
        psi = two(eCurr, nexp, even, dx, extra, None)
        lastPsi = lastpsi(psi)
        if lastPsi > 0:
            eLowFound = True
            eLow = eCurr
        if lastPsi < 0:
            eHighFound = True
            eHigh = eCurr
        eCurr += someE
    eCurr = (eHigh + eLow)/2
    stdev = abs(eHigh - eLow)
    i = 0
    while stdev > etol:
        psi = two(eCurr, nexp, even, dx, extra, None)
        lastPsi = lastpsi(psi)
        if lastPsi > 0:
            eLow = eCurr
        if lastPsi < 0:
            eHigh = eCurr
        eCurr = (eHigh + eLow)/2
        stdev = abs(eHigh - eLow)
        i += 1
    #print i
    if draw != None:
        psip = two(eCurr+stdev, nexp, even, dx, extra, draw)
        psim = two(eCurr-stdev, nexp, even, dx, extra, draw)
        draw.draw(psi, True, False)
        draw.draw(psip, True, False)
        draw.draw(psim, True, False)
    return eCurr, stdev

def four(etol, num, nexp, dx, extra, draw):
    print "N =", nexp
    eCurr = 0.1
    even = True
    n = 0
    while n < num:
        e, stdev = three(eCurr, etol, nexp, even, dx, extra, draw)
        es = e, stdev
        print e, stdev, math.sqrt(e)
        eCurr = e + 0.01
        even = not even
        n += 1

d = Draw()
print "printing E, deviation range, squareroot of E of m=0,1,2,3"
four(10**-15, 4, 2, 0.0001, 3, d)
four(10**-15, 4, 4, 0.0001, 3, d)
four(10**-10, 4, 8, 0.0001, 3, d)
four(10**-10, 4, 16, 0.0001, 3, d)
pylab.show()
