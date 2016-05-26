from itertools import combinations
t=int(input())
for _ in range(t):
    s=list(input())
    v=0
    f=0
    for k in range(len(s)//2+1):
        for l in combinations(s,k*2):
            r=''.join(j for j in l)
            c=r
            while len(r)>0:
                if r.count(r[0])%2!=0:
                    f=0
                    break
                else:
                    r=r.replace(r[0],'',r.count(r[0]))
                    f=1
            if f==1:
                v=v+len(c)//2
    print(v)
