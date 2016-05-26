import math
t=int(input())
for _ in range(t):
    a,b=[int(x) for x in input().split()]
    assert a<=10**9 and b<=10**9 and a>=1 and b>=1
    a=math.ceil(pow(a,0.5))
    b=math.floor(pow(b,0.5))
    print (int(b-a)+1)
