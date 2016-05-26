t=int(input())
for _ in range(t):
    l=[]
    n=int(input())
    v=(n-1)//3+1
    v=v*(v-1)*3//2
    l=(n-1)//5+1
    l=l*(l-1)*5//2
    m=(n-1)//15+1
    m=m*(m-1)*15//2
    print(v+l-m)
