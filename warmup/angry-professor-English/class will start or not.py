n=int(input())
assert n>0 and n<11
def check(b):
    j=1
    while abs(b)!=b or b==0:
        return j
for _ in range(0,n):
    k=list(map(int,input().split()))
    assert k[0]<1001 and k[0]>0
    assert k[1]<=k[0] and k[1]>0
    l=list(map(int,input().split()))
    assert len(l)==k[0]
    y=list(map(check,l))
    if y.count(1)>=k[1]:
        print("NO")
    else:
        print("YES")
