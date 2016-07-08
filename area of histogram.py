n=list(map(int,input().split()))
s=[]
maxarea=0
for i in range(len(n)+1):
    if len(s)>0:
        if n[i]>n[s[-1]] and i<len(n):
           s.append(i)
           print('append',s)
        else:
            print('1st else')
            print(s)
            while(len(s)!=0 and n[s[-1]]>n[i]):
                top=s.pop()
                if len(s)==0:
                    print('1st if')
                    area=n[0]*i
                    s.append(i)
                else:
                    print('stack is not empty')
                    print(s,i)
                    area=n[top]*(i-s[-1]-1)
                    print('area',area)
                if area>maxarea:
                    maxarea=area
                
    else:
        print('stack is empty appending')
        s.append(i)
