t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    assert len(l)==2
    b,w=l[0],l[1]
    l=list(map(int,input().split()))
    assert len(l)==3
    x,y,z=l[0],l[1],l[2]
    if x<y:
        q=x*b
        if x+z<y:
            w=(x+z)*w
        else:
            w=y*w
        print(q+w)
    else:
        q=y*w
        if y+z<x:
            w=(y+z)*b
        else:
            w=x*b
        print(q+w)
