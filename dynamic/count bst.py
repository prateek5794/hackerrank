n=5
t=[0 for k in range(n+1)]
t[0],t[1]=1,1
for i in range(2,n+1):
    for j in range(i):
        t[i]+=t[j]*t[i-j-1]
print(t[n])
