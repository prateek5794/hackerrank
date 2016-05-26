from math import sqrt
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    try:
        if(l[0]<0):
            raise ValueError
        j=sqrt(l[0]*l[0]+4*l[1])
        if(int(j)<j):
            raise ValueError
        k=(j+l[0])/2
        i=k-l[0]
        if(abs(i)!=abs(k)):
            print('4')
        else:
            if(l[1]==0):
                print('1')
            else:
                print('2')
    except ValueError:
        print('0')
    
