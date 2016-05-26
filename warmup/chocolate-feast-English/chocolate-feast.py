T = int(input())

for i in range(T):

    N,C,M = input().split()
    j=int(int(N)/int(C))
    if j<int(M):
        print(j)
    else:
        r=j
        while r>=int(M):
            j=j+int(r/int(M))
            r=int(int(r)/int(M))+r%int(M)
        print(j)
