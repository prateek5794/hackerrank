a='agbdefba'
n=len(a)
d=[[0 for k in range(n)] for k in range(n)] # initialising 2d array
for i in range(n):
    d[i][i]=1
for L in range(2, n+1):#level starts from 1 a n*n matrix(7*7)
    for i in range(0, n-L+1):
        j = i+L-1
        if a[i]==a[j]: # if first and last letter of subsequence are same than left below digonal+2
            d[i][j]=d[i+1][j-1]+2
        else:
            d[i][j]=max(d[i][j-1],d[i+1][j]) # if not max of left and below
l=[]
l2=[]
def tra(r,c):
    if c<r:
        return
    elif d[r][c]==d[r][c-1] and d[r][c]!=1:
        print('bagal')
        tra(r,c-1)
    elif d[r][c]==d[r+1][c] and d[r][c]!=1:
        print('niche')
        tra(r+1,c)
    elif d[r][c]==d[r+1][c-1]+2:
        print('diag+2')
        l.append(a[r])
        tra(r+1,c-1)
    else:
        print('diag+1')
        if a[r]==a[c]:
            l2.append(a[r])
        else:
            l2.append(a[r])
            l2.append(a[c])
        tra(r+1,c-1)
print(d[0][n-1])
tra(0,n-1)
k=[]
for j in l2:
    k.append(l+list(j))
l.reverse()
j=[]
for t in k:
    j.append(t+l)
