def lcs(p,s):
    j=len(s)
    i=len(p)
    l=[[0 for x in range(j+1)] for x in range(i+1)]
    o=[]
    for k in range(i+1):
        l[k][0]=0
    for k in range(j+1):
        l[0][k]=0
    for k in range(1,i+1):
        for q in range(1,j+1):
            if(p[k-1]==s[q-1]):
                l[k][q]=l[k-1][q-1]+1
                print(k-1,q-1)
                o.append(p[k-1])
            else:
                l[k][q]=max(l[k-1][q],l[k][q-1])
    print(o)
    return l[k][q],l
p='ZADBAVCEB'
s='ZABACEB'
o,l=lcs(p,s)
i=len(p)
print(o)
for k in range(i+1):
    print(l[k])


