n=int(input())
s=input()
k=int(input())
l=[]
for d in s:
    if(ord(d) in range(65,91)):
        j=ord(d)+k
        if(j>90):
            l.append(chr(64+j%90))
        else:
            l.append(chr(j))
    elif(ord(d) in range(97,123)):
        j=ord(d)+k
        if(j>122):
            l.append(chr(96+j%122))
        else:
            l.append(chr(j))
    else:
        l.append(d)
str1=''.join(l)
print(str1)
