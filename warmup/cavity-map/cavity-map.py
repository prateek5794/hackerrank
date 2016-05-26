n=int(input())
assert n>0 and n<101
lol=[]
for _ in range(n):
    k=list(map(int,input()))
    assert len(k)==n
    lol.append(k)
for k in range (n):
    q=[]
    if k>0 and k<n-1:
        for l in range(1,n-1):
            if type(lol[k][l])==int and type(lol[k][l-1])==int and type(lol[k][l+1])==int and type(lol[k-1][l])==int and type(lol[k+1][l])==int:
                if lol[k][l]>lol[k][l-1] and lol[k][l]>lol[k][l+1] and lol[k-1][l]<lol[k][l] and lol[k+1][l]<lol[k][l]:
                    q.append(l)
        for o in q:
            lol[k][o]='X'
        str1 = ''.join(str(e) for e in lol[k])
        print(str1)
    else:
        str1 = ''.join(str(e) for e in lol[k])
        print(str1)
