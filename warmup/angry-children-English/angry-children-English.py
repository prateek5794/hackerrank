n=int(input())
k=int(input())
l=[]
l2=[]
for _ in range(n):
    l.append(int(input()))
l.sort()
for j in range(n-k+1):
    l2.append(l[j+k-1]-l[j])
print(min(l2))
