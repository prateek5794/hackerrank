t=int(input())
for _ in range(t):
    l=[]
    a=list(input())
    b=list(input())
    if len(a)!=len(b):
        a,b=min(a,b,key=len),max(a,b,key=len)
    j,k=0,0
    while j<len(a):
        if a[j]<=b[k]:
            l.append(a.pop(j))
        else:
            l.append(b.pop(k))
    for f in b:
        l.append(f)
    print(''.join(l))
