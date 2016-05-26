n=input()
li=[]
li2=[]
l=0
for k in n.split():
    li.append(k)
list=[]
list2=[]
y=input()
for f in y.split():
    li2.append(int(f))
for k in range(int(li[1])):
    w=input()
    for h in w.split():
          list.append(int(h))
          l+=1
    m=min(li2[list[l-2]:list[l-1]+1])
    list2.append(m)
for a in list2:
    print(a)
