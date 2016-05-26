t=int(input())
for _ in range(t):
    l=list(map(int,input().strip().split()))
    if l[0]==1:
        print(l[1])
    else:
        k=pow(l[1],l[0]-1)
        print(k*(l[1]-1))
