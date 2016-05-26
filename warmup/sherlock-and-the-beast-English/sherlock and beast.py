t=int(input())
for _ in range(t):
    n=int(input())
    lis=[5,5,5]
    lis2=[3,3,3,3,3]
    if n>2 and n!=4 and n!=7:
        k=int(n/3)
        if n%3==0:
            lis=lis*k
            str1=''.join(str(e) for e in lis)
            print(str1)
        else:
            if n%3==1:
                lis=lis*(k-3)+lis2*2
                str1=''.join(str(e) for e in lis)
                print(str1)
            elif n%3==2:
                lis=lis*(k-1)+lis2
                str1=''.join(str(e) for e in lis)
                print(str1)
    else:
        print('-1')
