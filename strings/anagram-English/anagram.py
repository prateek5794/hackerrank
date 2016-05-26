t=int(input())
for _ in range(t):
    s=input()
    if len(s)%2==1:
        print('-1')
        continue
    else:
        x=int(len(s)/2)
        for k in range(x):
                s=s[:x]+s[x:].replace(s[k],'',1)
    print(len(s[x:]))
