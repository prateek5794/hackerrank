t=int(input())
for _ in range(t):
    l=[]
    n=int(input())
    v=(n-1)//3+1
    w=(v-1)*3
    V=v*w//2
    l=(n-1)//5+1
    r=(l-1)*5
    L=l*r//2
    m=(n-1)//15+1
    y=(m-1)*15
    M=m*y//2
    print(V+L-M)
