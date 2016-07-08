l=[3,4,5,6,8]
n=15
m=[[0 for k in range(n+1)]for k in range(len(l))]
for k in range(len(l)):
    m[k][0]=True
for k in range(1,n+1):
    m[0][k]=False
m[0][l[0]]=True
for i in range(1,len(l)):
    for j in range(1,n+1):
        if l[i]>j:
            m[i][j]=m[i-1][j]
        elif m[i-1][j]==True:
            m[i][j]=True
        else:
            m[i][j]=m[i-1][j-l[i]]
a=[]        
def tra(v,u):  #tracing back which element are in the bag
    if v==0:
        return
    if m[v][u]==m[v-1][u]: #checking if the current value is equal to tha upar wali value
        tra(v-1,u)
    else:  # if not then call recusion on the upper row and column - weight of elemrnt in knapsack
        a.append(l[v])
        tra(v-1,u-l[v])
tra(len(l)-1,n)
if m[len(l)-1][n]==True:
    print("possible")
print(a)
