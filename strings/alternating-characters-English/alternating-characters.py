t=int(input())
for _ in range(t):
    g=0
    n=input()
    for k in range(len(n)-1):
        assert n[k]=='A' or n[k]=='B'
        if n[k]==n[k+1]:
            g+=1
    print(g)
