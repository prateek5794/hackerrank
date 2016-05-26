n=int(input())
t=int(input())
list=[]
list2=[]
for k in range(n):
    list.append(int(input()))
for k in range(t):
    i=int(input())
    j=int(input())
    m=min(list[i:j+1])
    list2.append(m)
for a in list2:
    print(a)
