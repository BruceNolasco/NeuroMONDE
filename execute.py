import pickle
import MtoNCoupling as cp
Co60 = open("Co60cut.txt","r")
for l in Co60:
	signals= l.split("\t")
	num_sig = []
	print signals
	for s in signals:
		num_sig.append(float(s))
	net = pickle.load(open("nets/icnone.nmnd","rb"))
	result = net.feedforward(num_sig)
	print cp.binToCoord(result,8)