p=int(input())
q=int(input())
st=''
for k in range(p,q+1):
    s=str(k*k)
    if k==1:
        st='1 '
    if len(s)==1:
        pass
    else:
        if int(s[0:int(len(s)/2)])+int(s[int(len(s)/2):])==k:
            st=st+str(k)+' '
if len(st)==0:
    print('INVALID RANGE')
else:
    print(st)
