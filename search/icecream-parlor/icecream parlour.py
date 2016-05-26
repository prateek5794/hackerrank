t=int(input())
for _ in range(t):
    q=0
    m=int(input())
    N=int(input())
    n=list(map(int,input().split()))
    for k in range(len(n)):
        for l in range(k+1,len(n)):
            if n[k]+n[l]==m:
                q=1
                break
        if q==1:
            break
    print(str(k+1)+' '+str(l+1))
