import numpy as np
import MtoNCoupling as cp
#import mnist_loader as mn
import network

print "Welcome to NEUROMONDE SGD Training Tool"
print "Enter the number of gens: "

gens =int(raw_input())
topology = [16,32,32,16]
print "Defaults are T="+str(topology)
askplot = raw_input("Plot? Y/n  ")

traindata = cp.getTrainData("relSignalsC.txt","pointListC.txt")[::2]
net = network.Network([16,32,32,16])
test_data = [(x[0],cp.binToCoord(x[1],8))for x in traindata [::60]]

net.SGD(traindata,gens,100,0.1,test_data=test_data)

if askplot == "Y":

	import matplotlib.pyplot as plt
	means =[x[0] for x in net.history]
	stds = [float(x[1]) for x in net.history]

	base = [j for j in range(gens)]
	mini = [ x[2] for x in net.history]
	maxi = [ x[3] for x in net.history]
	minimax = []
	minimax.append([mini])
	minimax.append([maxi])

	fig, ax = plt.subplots()
	ax.errorbar(base, means, yerr =stds)
	ax.plot(base,mini,color="red")
	ax.plot(base,maxi,color="green")
	plt.show()

