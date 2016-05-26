n=int(input())
assert n%2!=0
l=list(map(int, input().split()))
assert len(l)==n
for k in range(0,int((len(l)+1)/2)):
    q=l.pop(0)
    try:
        l.remove(q)
    except ValueError:
        print(q)
