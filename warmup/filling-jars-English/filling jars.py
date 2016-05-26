n,m=map(int,input().split())
to=0
for _ in range(m):
    a,b,k=map(int,input().split())
    to+=(b-a)*k +k
print(int(to/n))
