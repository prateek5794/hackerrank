import itertools
n=int(input())
for _ in range(n):
    sumf,e,a=0,0,[]
    l=list(map(int,input().split()))
    a=list(map(int,input().split()))
    for k in range(1,l[0]+1):
        L=itertools.combinations(a,k)
        for q in L:
            sum=0
            for w in q:
                sum+=w
            h=sum%l[1]
            if(h==l[1]-1):
                sumf=h
                e=1
                break
            elif(sumf<h):
                sumf=h
        if(e==1):
            break
    print(sumf)
