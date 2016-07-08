import sys
t=[10,12,16,21]
f=[4,2,6,3]
n=len(f)
m = [[0 for x in range(n)] for x in range(n)]
for i in range(n):
    m[i][i]=f[i]
for L in range(2, n+1):#level starts from 1 a n*n matrix(4*4)
    for i in range(0, n-L+1):
        j = i+L-1
        su=sum(f[k] for k in range(i,j+1))
        mi=sys.maxsize
        for k in range(i,j+1):
            if k==i:
                q=m[k+1][j]
            elif k==j:
                q=m[i][j-1]
            else:
                q=m[i][k-1]+m[k+1][j]
            if q<mi:
                mi=q
        m[i][j]=su+mi  
print(m[0][n-1])
