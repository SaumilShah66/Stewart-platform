import csv
from math import sqrt
import pickle
import numpy as np
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)
file_name="trained_neural_net_3_2000_2000"
fileObject = open(file_name,'r') 
net= pickle.load(fileObject)
errors__=[]
true=[]
# from_net=[]
# for_tx_error_calculation=[]                    #error in tx
error=[0,0,0,0,0,0]



with open('data.csv','r') as csvfile:
	reader = csv.reader(csvfile)
	print "reading data"
	for row in reader:
		l=row[0:6]								#lengths input
		true.append(row[6:11])					#true output
		pd=net.activate(l)						#Output from ANN
		for i in range(6):
			error[i]=float(row[i+6])-float(pd[i])
		errors__.append(np.array(error))
		print type(error)
		print type(errors__)
		
		 # for_tx_error_calculation.append(true[0])
csvfile.close()
# print er


print "Writing Errors"
with open('errors_3_2000_2000.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for row in errors__:
        thedatawriter.writerow(row)
mycsvfile.close()