st=input()
n=int(st)
j=0
g=0
for e in st:
    j+=int(e)
k=2
l=[]
while k<=n:
    if n%k==0:
        l.append(k)
        n=int(n/k)
    elif n==1:
        break
    else:
        k+=1
str1=''.join(str(k) for k in l)
for k in str1:
    g+=int(k)
if g==j:
    print('1')
else:
    print('0')
