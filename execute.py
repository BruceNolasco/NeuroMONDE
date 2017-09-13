#Se improtan los modulos pickle para lectura de archivos
#MtoNCoupling para 
import pickle
import MtoNCoupling as cp
import numpy as np
Co60 = open("Co60cut.txt","r")
treshold = 0.2
for l in Co60:
	ot = 0
	signals= l.split("\t")
	num_sig = []
	nrm_sig = []
	for s in signals:
		num_sig.append(float(s))
	if max(num_sig)!=0:
		for s in num_sig:
			nrm_sig.append(s/max(num_sig))
		for s in nrm_sig:
			if s>= 0.2:
				ot+=1
		if ot>= 3:
			fin_sig = np.reshape(nrm_sig,(16,1))
			net = pickle.load(open("nets/icnone.nmnd","rb"))
			result = net.feedforward(fin_sig)
			binR = []
			for r in result:
				binR.append(r[0])
			coords = cp.binToCoord(binR,8)
			print coords[0],"\t",coords[1],"\t",ot
		