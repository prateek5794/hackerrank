n=list(map(int,input().split()))
assert len(n)==2
m=[]
lis=[]
lis2=[]
for _ in range(n[0]):
    m.append(int(input(),2))
for k in range(n[0]-1):
    for l in range(k+1,n[0]):
        lis.append(bin(m[k]|m[l]))
m=list(map(str,lis))
for k in range(len(m)):
    lis2.append(m[k].count('1'))
print(max(lis2))
print(lis2.count(max(lis2)))
