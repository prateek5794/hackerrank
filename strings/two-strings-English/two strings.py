t=int(input())
for _ in range(t):
    k=0
    a=input()
    b=input()
    if len(a)!=len(b):
        c=min(a,b,key=len)
        d=max(a,b,key=len)
    else:
        c=a
        d=b
    for j in c:
        if d.find(j)!=-1:
            print('YES')
            k=1
            break
    if k==0:
        print('NO')
