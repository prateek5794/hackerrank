import sys
l=[1,2,3,6,7]
n=21
c=[sys.maxsize for k in range(n+1)]
c[0]=0
co=[-1 for k in range(n+1)]
for j in range(len(l)):
    for k in range(n+1):
        if l[j]<=k:
            c[k]=min(c[k],1+c[k-l[j]])
            if c[k]>=1+c[k-l[j]]:
                co[k]=j
print(c)
o=[]
def tac(n):
    if n==0:
        return
    else:
        o.append(l[co[n]])
        tac(n-l[co[n]])
tac(len(co)-1)
print(o)
            
