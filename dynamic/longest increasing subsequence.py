n=[3,6,4,8,5]
t=[1 for k in range(len(n))]
for i in range(1,len(n)):
    for j in range(i):
        if n[j]<n[i]:
            t[i]=max(t[i],t[j]+1)
print(max(t))
