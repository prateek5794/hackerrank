n=int(input())
assert n>0 and n<1001
l=list(map(int,input().split()))
assert len(l)==n
while len(l)>0:
    l=list(map(lambda x:x-min(l),l))
    print(len(l))
    for _ in range(l.count(0)):
        l.remove(0)
    
