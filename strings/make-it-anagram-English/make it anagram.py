a=input()
b=input()
if len(a)!=len(b):
    c=list(min(a,b,key=len))
    d=list(max(a,b,key=len))
else:
    c=list(a)
    d=list(b)
l=abs(len(a)-len(b))
for k in c:
    try:
        d.remove(k)
    except ValueError:
        l+=2
print(l)
