t=int(input())
for _ in range(t):
    r=0
    l=list(map(int,input().split()))
    k=int(pow(l[0],0.5))+1
    q=k*k
    if pow(k-1,2)==l[0]:
        r=1
    if q<=l[1]:
        while q<=l[1]:
            q=q+2*k+1
            k+=1
            r+=1
        print(r)
    else:
        print(r)
