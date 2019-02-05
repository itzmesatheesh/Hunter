a=input("")
length=int(len(a))
for i in range(0, int(length/2 + 1)):
   if a[i]==a[-i - 1]:
      i+=1
   else:
      break
if i<(length / 2):
   print("NO")
else:
   print("YES")
