m=int(input())
n=int(input())
k=[]
h=0
b=[]
for _ in range(m):
    l=list(map(int,input().split()))
    k.append(l)
for i in range(m):
    for j in range(n):
        if(k[i][j]==1):
            h+=1
            try:
                if(j==0):
                    if(i!=m-1):
                        if(k[i][j+1]==1 or k[i+1][j]==1 or k[i+1][j+1]==1):
                            pass
                        else:
                            b.append(h)
                    else:
                        if(k[i][j+1]==1):
                            pass
                        else:
                            b.append(h)
                elif(j==n-1):
                    if(i!=m-1):
                        if(k[i+1][j]==1 or k[i+1][j-1]==1):
                            pass
                        else:
                            b.append(h)
                    else:
                        b.append(h)
                elif(i!=m-1):
                    if(k[i][j+1]==1 or k[i+1][j]==1 or k[i+1][j+1]==1 or k[i+1][j-1]==1):
                        pass
                    else:
                        b.append(h)
                else:
                    if(k[i][j+1]==1):
                        pass
                    else:
                        b.append(h)
            except ValueError:
                pass        
print(max(b))
