from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import csv
import pickle


i=1
# creting dataset
ds = SupervisedDataSet(6, 6)
with open('data.csv','r') as csvfile:
	reader = csv.reader(csvfile)
	print "reading data"
	for row in reader:
		ds.addSample(row[0:6],row[6:])
		if i>2000:
			break
		i=i+1
print "data has benn read"
print len(ds)




# creating network
net = buildNetwork(6, 6, 6,bias=True)
# net = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)

# training network
print "network created"
trainer = BackpropTrainer(net, ds,momentum=0.01, verbose=True, learningrate = 0.5)
print "now training the network"

trainer.trainUntilConvergence(dataset=ds, maxEpochs=200, verbose=True, validationProportion=0.25)
trainer1=BackpropTrainer(net, ds,momentum=0.9, verbose=True, learningrate = 0.01)

trainer1.trainUntilConvergence(dataset=ds, maxEpochs=200, verbose=True, validationProportion=0.25)
trainer2=BackpropTrainer(net, ds,momentum=0.01, verbose=True, learningrate = 0.0001)
trainer2.trainUntilConvergence(dataset=ds, maxEpochs=200, verbose=True, validationProportion=0.25)

# for i in range(100):
# trainer.trainUntilConvergence()
# trainer.train()
file_name="trained_neural_net_testingTW"
fileObject=open(file_name,'wb')
pickle.dump(net,fileObject)
fileObject.close()
