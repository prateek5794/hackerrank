a='abcdba'
b='abdcba'
d=[[0 for k in range(len(a)+1)] for k in range(len(b)+1)] # initialising 2d array
for i in range(1,len(b)+1): #calculating the lcs
    for j in range(1,len(a)+1):
        if b[i-1]==a[j-1]:
            d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=max(d[i-1][j],d[i][j-1])
print(d[len(b)][len(a)])
l=[]
def track(u,v): #tracking back the lcs
    if u==0 and v==0:
        print('return')
        return
    elif d[u][v]==d[u-1][v]:
        print('upar wala')
        track(u-1,v)
    elif d[u][v]==d[u][v-1]:
        print('bagal wala')
        track(u,v-1)
    else:
        print('diag wala')
        l.append(b[u-1]) #appending the word to list l
        track(u-1,v-1)
track(len(b),len(a))
l.reverse()
print(l)
