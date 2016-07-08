a='abcdaf'
b='zbcdf'
d=[[0 for k in range(len(a)+1)] for k in range(len(b)+1)] # initialising 2d array
for i in range(1,len(b)+1): #calculating the lcs
    for j in range(1,len(a)+1):
        if b[i-1]==a[j-1]:
            d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=0
q=-1
for k in d:
    if max(k)>q:
        q=max(k)
        j=k
print('longest substring is ',q)
l=[]
def track(u,v): #tracking back the lcs
    if d[u][v]==0:
        return
    else:
        l.append(b[u-1]) #appending the word to list l
        track(u-1,v-1)
track(d.index(j),j.index(q))
l.reverse()
s=''
for k in l:
   s+=k
print(s)
