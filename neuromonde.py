import numpy as np
import MtoNCoupling as cp
#import mnist_loader as mn
import network
import pickle

print "Welcome to NEUROMONDE SGD Training Tool"
print "Enter the number of gens: "

gens =int(raw_input())
topology = [16,32,32,32,16]
print "Defaults are T="+str(topology)
askload = raw_input("Load or new net? L/N:  ")
identifier = raw_input("Run identifier? ")
save_history = raw_input("Save history? Y/n ")
askplot = raw_input("Plot? Y/n  ")
if askplot == "Y":
	askerrors = raw_input("Error bars? Y/n  ")
traindata = cp.getTrainData("relSignalsC.txt","pointListC.txt")[::2]

if askload == "L":
	net = pickle.load(open("nets/"+identifier+".nmnd","rb"))
else:
	net = network.Network(topology)
test_data = [(x[0],cp.binToCoord(x[1],8))for x in traindata [::60]]

net.SGD(traindata,gens,100,0.04,test_data=test_data)

if askplot == "Y":
	import matplotlib.pyplot as plt
	means =[x[0] for x in net.history]
	stds = [float(x[1]) for x in net.history]

	base = [j for j in range(len(means))]
	mini = [ x[2] for x in net.history]
	maxi = [ x[3] for x in net.history]
	minimax = []
	minimax.append([mini])
	minimax.append([maxi])

	fig, ax = plt.subplots()
	if askerrors == "Y":
		ax.errorbar(base, means, yerr =stds)
	else:
		ax.plot(base,means)
	ax.plot(base,mini,color="red")
	ax.plot(base,maxi,color="green")
	plt.show()

if identifier != "":
	if save_history!="Y":
		net.history=[]
	pickle.dump(net, open("nets/"+identifier+".nmnd","wb"))
