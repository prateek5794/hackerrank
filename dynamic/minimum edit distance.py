a='abcdef'
b='azced'
m=[[0 for k in range(len(a)+1)] for k in range(len(b)+1)]
for i in range(len(a)+1):
    m[0][i]=i
for i in range(len(b)+1):
    m[i][0]=i
for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        if b[i-1]==a[j-1]:
            m[i][j]=m[i-1][j-1]
        else:
            m[i][j]=min(m[i-1][j-1],m[i-1][j],m[i][j-1])+1
print(m[len(b)][len(a)])
t=[]
def tra(r,c):
    if r==0 and c==0:
        return
    elif m[r][c]==m[r-1][c-1] and b[r-1]==a[c-1]:
        print(r,c)
        print('first')
        tra(r-1,c-1)
    elif m[r][c]==m[r][c-1]+1:
        print(r,c)
        print('second')
        t.append('delete')
        tra(r,c-1)
    else:
        print(r,c)
        print('else')
        t.append('edit')
        tra(r-1,c-1)
tra(len(b),len(a))
print(t)
