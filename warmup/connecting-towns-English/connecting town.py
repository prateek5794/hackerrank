n=int(input())
for _ in range(n):
    j=1
    x=int(input())
    l=list(map(int,input().split()))
    for k in l:
        j*=k
    print(j%1234567)
