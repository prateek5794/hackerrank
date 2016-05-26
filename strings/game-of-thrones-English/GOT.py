s=input()
l=0
k=0
while k<len(s):
    g=s.count(s[k])
    if g%2!=0:
        l+=1
    s=s.replace(s[k],'',g)
    k+=1
if l>1:
    print('NO')
else:
    print('YES')