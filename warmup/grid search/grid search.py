n=int(input())
for _ in range(n):
    k,j,h=[],[],0
    l=list(map(int,input().split()))
    for _ in range(l[0]):
        k.append(input())
    l=list(map(int,input().split()))
    for _ in range(l[0]):
        j.append(input())
    q=-1
    for l in k:
        if(h<len(j)):
            if(q!=-1 and l.find(j[h])==-1):
                q=-1
                break
            q=l.find(j[h])
        else:
            break
        if(q!=-1):
            h+=1
    if(q==-1):
        print('NO')
    else:
        print('YES')
