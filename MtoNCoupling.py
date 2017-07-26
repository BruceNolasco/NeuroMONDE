import numpy as np

def nToBin (n,m):
# Receives an intenger n and transcribes it to a vector of m bits
    b = []
    for i in range(m):
        r = int((n%(2**(i+1)))/(2**(i)))
        b.append(r)
        n -= r
    return b

def binToN (b):
#Receiver a Bin a-like vector and return the natural number it represents
    m = len(b)
    n = 0
    #print "B :"
    #print b
    for i in range(m):
        """if b[i]>= 0.6:
            b[i] = 1
        else:
            b[i] = 0"""
        n+=b[i]*(2**i)
    #print n
    return int(n)

def coordToBin(x,y,m1,m2):
    #receives a pair of coordinates and the m numbers of the bit-lenght of each one
    b = nToBin(x,m1)
    for x in nToBin(y,m2):
        b.append(x)
    return b


def binToF (b):
#Receiver a Bin a-like vector and return the natural number it represents
    m = len(b)
    n = 0
    #print "B :"
    #print b
    for i in range(m):
        """if b[i]>= 0.6:
            b[i] = 1
        else:
            b[i] = 0"""
        n+=b[i]*(2**i)
    #print n
    return float(n)

def binToCoordF(b,m):
    #receives a Bin alike vector and the m lenght of the first byte outputs a pair of x,y coords
    #print b
    x = binToF(b[:m])
    y = binToF(b[m:])
    return (x,y)


def binToCoord(b,m):
    #receives a Bin alike vector and the m lenght of the first byte outputs a pair of x,y coords
    if len(b)==1:
        b = b[0]
    #print b
    x = binToN(b[:m])
    y = binToN(b[m:])
    return (x,y)

def getPointListForNeuron(pointListFile):
    pointList = open(pointListFile,"r")
    pointListArray = []

    for point in pointList:
        splitted = []
        splitted = point.split()
        for i in range(2):
            splitted[i]= float(splitted[i])
            splitted[i]= int(splitted[i])
        Bin = np.zeros((16,1))
        x = coordToBin(int(splitted[0]),int(splitted[1]),8,8)
        for i in range(len(Bin)):
            Bin[i] = x[i]
        #print Bin
        #Bin = np.reshape(Bin,(16,1))
        pointListArray.append(Bin)
        #print pointListArray
    return np.asarray(pointListArray)

def getRelSigsForNeuron(relSigsFile):
    relSigs = open(relSigsFile,"r")
    relSigsArray = []

    for signal in relSigs:
        splitted = []
        splitted = signal.split()
        for i in range(16):
            splitted[i]= float(splitted[i])
        #print splitted
        #splitted = np.array(splitted)
        relSigsArray.append([splitted])
    return np.asarray([np.reshape(x,(16,1)) for x in relSigsArray])

def getTrainData(relSigsFile,pointListFile):
    return [(x,y) for x,y in zip(getRelSigsForNeuron(relSigsFile),getPointListForNeuron(pointListFile))]

"""
#Local Test script
xraw  = int(raw_input("x: "))
yraw  = int(raw_input("y: "))
x = coordToBin(xraw,yraw,8,7)
print x
print binToCoord(x,8)

x = getTrainData("relSignalsC.txt","pointListC.txt")[20:30]

for i in x:
    print "Point (BIN): "+str(i[1])
    print "Point: "+str(binToCoord(i[1],8))
    print "Signal: "+str(i[0])
    print ""
"""
def eval (test_data):
    success = 0
    test_results = []
    for (x,y) in test_data:
    #    print "x: "+str(x)
        result = self.feedforward(x)
    #    print "Result"
    #    print result
        test_results.append((mn.binToCoord(result,8),y))
    #test_results = [ for (x,y) in test_data]
    print "Test results"
    print test_results
    for x in test_results:
        if x[0][0]==x[1][0] and x[0][1] == x[1][1]:
            success+=1
    return success
