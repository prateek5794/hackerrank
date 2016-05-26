t=int(input())   
for _ in range(t):
    f=0
    a,b=0,1
    n=int(input())
    while f<n:
        f=a+b
        a,b=b,f
    if f==n:
        print('IsFibo')
    else:
        print('IsNotFibo')
