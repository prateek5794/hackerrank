n=list(map(int,input().split()))
assert len(n)==2
m=[]
mt=0
st=0
z=0
for _ in range(n[0]):      #taking all team input
    m.append(input())
for k in range(n[0]-1):    #calculating max no. of topic a team can know
    for l in range(k+1,n[0]):
        kt=0
        for q in range(n[1]):
            if int(m[k][q]) or int(m[l][q]):
                kt+=1
        if kt>mt:
            mt=kt
        if kt==n[1]:
            z='a'
            break
    if z=='a':
        break
for k in range(n[0]-1):  #calculating no. of pairs of team
    for l in range(k+1,n[0]):
        kt=0
        for q in range(n[1]):
            if int(m[k][q]) or int(m[l][q]):
                kt+=1
        if kt==mt:
            st+=1
print(mt)
print(st)
