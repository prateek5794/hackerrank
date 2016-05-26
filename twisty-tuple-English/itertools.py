n=int(input())
s=list(map(int,input().strip().split()))
l=0
for i in range(len(s)-2):
    a_j=None
    k=0
    for j in range(i+1,len(s)):
        mini=s[i]
        if(s[j]>mini):
            if(a_j==None):
                a_j=s[j]
            k+=1
        elif(a_j!=None and s[j]<mini):
            l+=k
print(l)
