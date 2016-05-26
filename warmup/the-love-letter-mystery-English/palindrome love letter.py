import math
k=int(input())
li=[]
list=[]
for j in range(k):
    y=input()
    list.append(y)
for l in list:
    h=len(l)
    k=math.floor(h/2)
    o=0
    for u in range(k):
        while l[u]>l[len(l)-1-u] :
            if u==0:
                l=chr(ord(l[u])-1)+l[u+1:]
            else:
                l=l[:u]+chr(ord(l[u])-1)+l[u+1:]
            o+=1
        while l[u]<l[len(l)-1-u]:
            if u==0:
                l=l[:len(l)-1-u]+chr(ord(l[len(l)-1-u])-1)
            else:
                l=l[:len(l)-1-u]+chr(ord(l[len(l)-1-u])-1)+l[len(l)-u:]
            o+=1
    li.append(o)
for h in li:
    print(h)
