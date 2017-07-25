import numpy as np

def nToBin (n,m):
# Receives an intenger n and transcribes it to a vector of m bits
    b = []
    for i in range(m):
        r = int((n%(2**(i+1)))/(2**(i)))
        b = np.append(b,r)
        n -= r
    return b

def binToN (b):
#Receiver a Bin a-like vector and return the natural number it represents
    m = len(b)
    n = 0
    for i in range(m):
        n+=b[i]*(2**i)
    return int(n)

def coordToBin(x,y,m1,m2):
    #receives a pair of coordinates and the m numbers of the bit-lenght of each one
    b = nToBin(x,m1)
    b = np.append(b,nToBin(y,m2))
    return b

def binToCoord(b,m):
    #receives a Bin alike vector and the m lenght of the first byte outputs a pair of x,y coords
    x = binToN(b[:m])
    y = binToN(b[m:])
    return (x,y)

xraw  = int(raw_input("x: "))
yraw  = int(raw_input("y: "))
x = coordToBin(xraw,yraw,8,7)
print x
print binToCoord(x,8)
