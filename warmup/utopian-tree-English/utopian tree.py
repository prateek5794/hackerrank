import math
k=input("enter the number of cycle:")
l=int(k)
w=0
list=[]
while w<l:
    c=input("enter input:")
    list.append(int(c))
    w+=1
for f in list:
    r=f/2
    x=math.ceil(r)
    if f%2==0 :
        d=pow(2,x+1)-1
        print(d)
    else:
        d=pow(2,x+2)-1
        print(d-1)
