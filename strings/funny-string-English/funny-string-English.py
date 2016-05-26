t=int(input())
for _ in range(t):
    l=0
    s=input()
    for k in range(len(s)-1):
        if abs(ord(s[k+1])-ord(s[k]))!=abs(ord(s[len(s)-k-2])-ord(s[len(s)-k-1])):
            l=1
            break
    if l==1:
        print('Not Funny')
    else:
        print('Funny')
