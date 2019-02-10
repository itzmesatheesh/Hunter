def hunter_37():
	a=input()
	b=len(a)
	c=''
	if(b%2!=0):
		c+=a[b//2+1:]
		c=c[::-1]
		if(a[:b//2]==c):
			print('Yes')
			return
	print('No')
try:
	hunter_37()
except:
	print('Invalid')
