from fractions import gcd
t=int(input())
for _ in range(t):
    s=0
    q=0
    n=int(input())
    a=list(map(int,input().split()))
    if a.count(1)!=0:
        print('YES')
        continue
    for k in a:
        for l in a[q+1:]:
            if gcd(k,l)==1:
                print('YES')
                s=1
                break
        if s==1:
            break
    if s==1:
        continue
    if s==0:
        print('NO')
        
