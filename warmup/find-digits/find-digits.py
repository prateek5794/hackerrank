t=int(input())
assert t>0 and t<16
for _ in range(t):
    j=input()
    assert int(j)>0 and int(j)<10000000000
    i=list(map(int,j))
    u=i.count(0)
    while u>0:
        i.remove(0)
        u-=1
    i=list(filter(lambda x:int(j)%x==0,i))
    print(len(i))
