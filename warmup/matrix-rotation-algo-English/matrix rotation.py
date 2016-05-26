from math import ceil
n=list(map(int,input().split()))
l=[]
lol=[]
for k in range(n[0]):
    l.append(list(map(int,input().split())))
while(len(l[0])!=0):
    a=[]
    for k in l.pop(0):
        a.append(k)
    for k in range(0,len(l)-1):
        a.append(l[k].pop())
    l[len(l)-1].reverse()
    for k in l.pop():
        a.append(k)
    for k in range(len(l)-1,-1,-1):
        a.append(l[k].pop(0))
    a=a[n[2]%len(a):]+a[:n[2]%len(a)]
    lol.append(a)
    try:
        len(l[0])
    except IndexError:
        break
j,y=0,0
l=[[] for x in range(n[0])]
for _ in range(len(lol)):
    h=j+1
    p=ceil(len(l[j])/2)
    for k in lol[j][:n[1]-y]:
        l[j].insert(p,k)
        p+=1
    for k in lol[j][n[1]-y:n[0]+n[1]-2-2*y  ]:
        l[h].insert(j,k)
        h+=1
    p=ceil(len(l[n[0]-j-1])/2)
    for k in lol[j][n[1]+n[0]-2-2*y:n[1]*2+n[0]-2-3*y]:
        l[h].insert(p,k)
    h-=1
    for k in lol[j][n[1]*2+n[0]-2-3*y:]:
        l[h].insert(j,k)
        h-=1
    j+=1
    y+=2
for k in l:
    str1=' '.join(str(e)for e in k)
    print(str1)
