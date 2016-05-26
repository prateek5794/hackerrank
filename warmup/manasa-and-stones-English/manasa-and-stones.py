t=int(input())
assert 0<t<11
for _ in range(t):
    q=[]
    n=int(input())
    a=int(input())
    b=int(input())
    m=min(a,b)
    k=m*(n-1)
    q.append(k)
    while k<max(a,b)*(n-1):
        l=abs(b-a)
        k+=l
        q.append(k)
    str1=''.join(str(e)+' ' for e in q)
    print(str1)
