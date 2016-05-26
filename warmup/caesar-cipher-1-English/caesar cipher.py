n=int(input())
s=input()
k=int(input())
l=[]
for d in s:
    if(ord(d) in range(65,91)):
        j=ord(d)+k
        if(j>90):
            if((j%90)%26!=0):
                l.append(chr(64+(j%90)%26))
            else:
                l.append('Z')
        else:
            l.append(chr(j))
    elif(ord(d) in range(97,123)):
        j=ord(d)+k
        if(j>122):
            if((j%122)%26!=0):
                l.append(chr(96+(j%122)%26))
            else:
                l.append('z')
        else:
            l.append(chr(j))
    else:
        l.append(d)
str1=''.join(l)
print(str1)
