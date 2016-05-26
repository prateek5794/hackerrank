n=input()
import math
k=math.sqrt(len(n))
f=math.floor(k)
c=math.ceil(k)
lol=[]
for j in range(0,c):
    l=[]
    for k in range(j,len(n),c):
        l.append(n[k])
    lol.append(l)
a=''
for k in range(len(lol)):
    str1=''.join(lol[k])
    a=a+str1+' '
print(a)
