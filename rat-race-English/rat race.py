n=int(input())
assert 1<=n<=100
s=list(map(int,input().strip().split()))
d=list(map(int,input().strip().split()))
lis=[]
for j,k in zip(s,d):
    lis.append(k/j)
m=min(lis)
c=lis.count(m)
k=1
for _ in range(c):
    print(lis.index(m)+k)
    lis.remove(m)
    k+=1
