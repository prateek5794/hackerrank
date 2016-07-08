N=[100,60,120]
W=[20,10,30]
w=50
d=[[0 for k in range(w+1)]for k in range(len(W)+1)]
a=[]
for i in range(1,len(d)): #finding the weight to maximise the value
    for j in range(1,len(d[0])):
        if W[i-1]>j:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(N[i-1]+d[i-1][j-W[i-1]],d[i-1][j])
def tra(v,u):  #tracing back which element are in the bag
    if v==0:
        return
    if d[v][u]==d[v-1][u]: #checking if the current value is equal to tha upar wali value
        tra(v-1,u)
    else:  # if not then call recusion on the upper row and column - weight of elemrnt in knapsack
        a.append(W[v-1])
        tra(v-1,u-W[v-1])
    
print(d[len(W)][w]) #printing the bottom right value of 2d array
tra(len(W),w)
print(a) #printing list of element inside the bag

