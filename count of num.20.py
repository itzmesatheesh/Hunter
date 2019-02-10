def hunt_20():
	x=int(input())
	y=int(input())
	z=0
	for i in range(x,y):
		if z!=1:
			z+=1
	print(z)
try:
	hunt_20()
except:
	print('Invalid')
