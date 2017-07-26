import numpy as np
import MtoNCoupling as cp
#import mnist_loader as mn
import network
import pickle

print "Welcome to NEUROMONDE SGD Training Tool (Heavy ED.)"
print "Enter the number of gens: "

gens =int(raw_input())
topology = [16,32,32,32,16]
print "Defaults are T="+str(topology)
identifier = ""

while identifier=="":
	identifier = raw_input("Run identifier? ")

traindata = cp.getTrainData("relSignalsC.txt","pointListC.txt")

net = network.Network(topology)
test_data = [(x[0],cp.binToCoord(x[1],8))for x in traindata [::140]]

net.SGDHeavy(traindata,gens,300,0.01,identifier,test_data=test_data)
pickle.dump(net, open("nets/"+identifier+".nmnd","wb"))
