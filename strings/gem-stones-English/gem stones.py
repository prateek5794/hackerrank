n=int(input())
l=[]
u=0
for _ in range(n):
    l.append(input())
c=min(l,key=len)
c=''.join(set(c))
for k in c:
    for m in range(len(l)):
        s=0
        if l[m].find(k)==-1:
            s=1
            break
    if s==0:
        u+=1
print(u)
