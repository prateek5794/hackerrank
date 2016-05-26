n=list(map(int,input().split()))
assert len(n)==2
m=[]
mt=0
st=0
s=0
z=0
for _ in range(n[0]):      #taking all team input
    m.append(input())
for k in range(n[0]-1):    #calculating max no. of topic a team can know and no. of team
    for l in range(k+1,n[0]):
        kt=0
        for q in range(n[1]):
            if int(m[k][q]) or int(m[l][q]):
                kt+=1
        if kt>mt:
            mt=kt
            s='a'
            st=0
        elif kt==mt and s=='a':
            st=0
            s='b'
        if kt==mt and s=='b':
            st+=1
            s='b'  
print(mt)
print(st+1)
