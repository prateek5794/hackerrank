t=int(input())
for _ in range(t):
    q=0
    s=list(input())
    for k in range(len(s)//2):
        if s[k]!=s[len(s)-1-k]:
            q=1
            if s[k]==s[len(s)-1-k-1] and s[k+1]==s[len(s)-1-k-2]:
                print(len(s)-1-k)
                break
            elif s[len(s)-1-k]==s[k+1] and s[len(s)-1-k-1]==s[k+2]:
                print(k)
                break
    if q==0:
        print('-1')
