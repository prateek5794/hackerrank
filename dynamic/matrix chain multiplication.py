import sys
p= [2,3,6,4,5]
n= len(p)
m = [[0 for x in range(n)] for x in range(n)]
for k in m:
        print(k)
for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            print(i,j)
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

print(m[1][n-1])
