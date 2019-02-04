a=input()
b=[]
res=''
for i in range(len(a)):
    if(a[i] not in b):
        b.append(a[i])
for i in range(len(b)-1,-1,-1):
    res+=b[i]
print(res)
