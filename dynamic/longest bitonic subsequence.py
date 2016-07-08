n=[2,-1,4,3,-2,-1,3,2]
def lis(n): #longest incresind subsequence
    t=[1 for k in range(len(n))]
    for i in range(1,len(n)):
        for j in range(i):
            if n[j]<n[i]:
                t[i]=max(t[i],t[j]+1)
    return t
k=lis(n)
n.reverse() #reverse the array
j=lis(n)
j.reverse() #reversing the array containing lis 
l=[]
for i,o in zip(k,j):
    l.append(i+o-1)
print(max(l))
