t=int(input())
for _ in range(t):
    q=0
    c=''
    w=list(input())
    for k in range(len(w)-2,-1,-1):
        if w[k]<w[k+1]:
            c=w[k]
            q=1
            break
    for j in range(k+1,len(w)):
        if w[j]>c:
            w[j],w[k]=w[k],w[j]
    if q==0:
        print('no answer')
    else:
        w=w[:k+1]+sorted(w[k+1:])
        print(''.join(w))
