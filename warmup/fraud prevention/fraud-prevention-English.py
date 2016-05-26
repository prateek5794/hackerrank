n=int(input())
l=[[] for k in range(n)]
for k in range(n):
    s=[]
    s.append(input().split(','))
    l[k]=list(map(lambda x:x.lower(),s[0]))
    l[k][2]=l[k][2].replace('.','')
    i=l[k][2].rfind('+')
    if(i!=-1):
        j=l[k][2].rfind('@')
        l[k][2]=l[k][2][:i]+l[k][2][j:]
    if(l[k][3].rfind(' street')!=-1):
        l[k][3]=l[k][3].replace(' street',' st.')
    if(l[k][3].rfind(' road')!=-1):
        l[k][3]=l[k][3].replace(' road',' rd.')
    if(l[k][5].rfind('new york')!=-1):
        l[k][5]=l[k][5].replace('new york','ny')
    if(l[k][5].rfind('california')!=-1):
        l[k][5]=l[k][5].replace('california','ca')
    if(l[k][5].rfind('illinois')!=-1):
        l[k][5]=l[k][5].replace('illinois','il')
    if(l[k][6].rfind('-')!=-1):
        l[k][6]=l[k][6].replace('-','')
q=[]
for k in range(n):
    for j in range(k+1,n):
        if(l[k][1]==l[j][1]):
            q.append(k+1)
            if(l[k][2]==l[j][2]):
                if(l[k][7]!=l[j][7]):
                    q.append(j+1)
                    break
            elif(l[k][3]==l[j][3] and l[k][4]==l[j][4] and l[k][5]==l[j][5] and l[k][6]==l[j][6]):
                if(l[k][7]!=l[j][7]):
                    q.append(j+1)
                    break
    q=list(set(q))
q.sort()
str1=','.join(str(e) for e in q)
print(str1)
