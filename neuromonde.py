import numpy as np
import MtoNCoupling as cp
#import mnist_loader as mn
import network
import matplotlib.pyplot as plt

gens = 20
traindata = cp.getTrainData("relSignalsC.txt","pointListC.txt")[::2]
net = network.Network([16,32,32,16])
test_data = [(x[0],cp.binToCoord(x[1],8))for x in traindata [::60]]
#print [(x[0],x[1]) for x in test_data]
#print traindata[:5]
#print mn.load_data_wrapper()[0][:1]
net.SGD(traindata,gens,100,0.1,test_data=test_data)

means =[x[0] for x in net.history]
stds = [float(x[1]) for x in net.history]

base = [j for j in range(gens)]
mini = [ x[2] for x in net.history]
maxi = [ x[3] for x in net.history]
minimax = []
minimax.append([mini])
minimax.append([maxi])
print minimax

fig, ax = plt.subplots()
ax.errorbar(base, means, yerr =stds)
ax.plot(base,mini,color="red")
ax.plot(base,maxi,color="green")
plt.show()

plt.show()
