def place(row,column,n):
    if(row==0):
        return True
    for k in range(row):
        if(l[k][column]==1):
            return False
    h=row
    j=column
    while(h>0 and j>0):
        h=h-1
        j=j-1
        if(l[h][j]):
            return False
    h=row
    j=column
    while(h>0 and j<n-1):
        h=h-1
        j=j+1
        if(l[h][j]):
            return False
    return True
def nqueen(row,n):
    for k in range(n):
        l[row-1][k]=0
    for column in range(n):
        if(place(row-1,column,n)):
            l[row-1][column]=1
            if(row==n):
                for i in range(n):
                    print(l[i])
                print('\n\n')
            else:
                nqueen(row+1,n)
                for k in range(n):
                    l[row-1][k]=0
                
n=int(input())
l=[[0 for x in range(n)] for x in range(n)]
nqueen(1,n)
input()
