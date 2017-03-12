import numpy as np 	
import csv
from math import *
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

def transformation(tx,ty,tz):
	Rx=np.array([
		[1				,0				,0],
		[0				,cos(tx)		,sin(tx)],
		[0				,-sin(tx)		,cos(tx)]])
	Ry=np.array([
		[cos(ty)		,0				,-sin(ty)],
		[0				,1				,0],
		[sin(ty)		,0				,cos(ty)]])
	Rz=np.array([
		[cos(tz)		,sin(tz)		,0],
		[-sin(tz)		,cos(tz)		,0],
		[0				,0				,1]])
	R=np.matrix(Rx)*np.matrix(Ry)*np.matrix(Rz)
	return(R)
def inverse_kinematics(base,top_fixed,tx,ty,tz,x,y,z):
	
	txx=float((10-tx))/20
	tyy=float((10-ty))/20
	tzz=float((10-tz))/20
	xx=float((10-x))/20.0
	yy=float((10-y))/20.0
	zz=float((50-z))/30.0
	tx=tx*(np.pi)/180
	ty=ty*(np.pi)/180
	tz=tz*(np.pi)/180
	R=transformation(tx,ty,tz)
	top=np.array(np.matrix(top_fixed)*np.matrix(R)) + [x,y,z]
	final=[0,0,0,0,0,0,txx,tyy,tzz,xx,yy,zz]
	
	for i in range(6):
		diff=top[i] - base[i]
		final[i]=sqrt(diff[0]**2 + diff[1]**2 + diff[2]**2)
		
	return(final)


 # 
R=50
theta=8*(3.14/180)
one_twenty=120*(3.14/180)
base=np.array([
	[R*cos(theta) 						,R*sin(theta) 						,0.0],
	[R*cos(one_twenty	- theta) 		,R*sin(one_twenty	- theta) 		,0.0],
	[R*cos(one_twenty 	+ theta) 		,R*sin(one_twenty 	+ theta)  		,0.0],
	[R*cos(2*one_twenty - theta) 		,R*sin(2*one_twenty - theta) 		,0.0],
	[R*cos(2*one_twenty + theta) 		,R*sin(2*one_twenty + theta) 		,0.0],
	[R*cos(-theta) 						,R*sin(-theta) 						,0.0]])
print base
top_fixed=np.array([
	[R*cos(one_twenty/2 	- theta) 	,R*sin(one_twenty/2 	- theta)	,0.0],
	[R*cos(one_twenty/2 	+ theta) 	,R*sin(one_twenty/2 	+ theta) 	,0.0],
	[R*cos(3*one_twenty/2 	- theta) 	,R*sin(3*one_twenty/2 	- theta) 	,0.0],
	[R*cos(3*one_twenty/2 	+ theta) 	,R*sin(3*one_twenty/2 	+ theta) 	,0.0],
	[R*cos(-one_twenty/2 	- theta)  	,R*sin(-one_twenty/2 	- theta) 	,0.0],
	[R*cos(-one_twenty/2 	+ theta) 	,R*sin(-one_twenty/2 	+ theta) 	,0.0]])
# print top_fixed
# print inverse_kinematics(base,top_fixed,0,0,0,0,0,15)
# print transformation(0,0,0)
k=1
max_len=80
min_len=40

data=[]
for Rx in range(-10,10,5):
	for Ry in range(-10,10,5):
		for Rz in range(-10,10,5):
			for x in range(-10,10,2):
				for y in range(-10,10,2):
					for z in range(20,50,5):
						final=inverse_kinematics(base,top_fixed,Rx,Ry,Rz,x,y,z)
						for i in range(6):
							final[i]=(max_len - final[i])/(max_len - min_len)
						# print l
						if 1>final[0]>0 and 1>final[1]>0 and 1>final[2]>0 and 1>final[3]>0 and 1>final[4]>0 and 1>final[5]>0:
							data.append(final)
							k=k+1
							print k,final
						
np.random.shuffle(data)
with open('data.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for row in data:
        thedatawriter.writerow(row)
    