t=int(input())
for _ in range(t):
    l=[]
    st='31415926535897932384626433833'
    s=list(input().split())
    for k in s:
        l.append(str(len(k)))
    str1=''.join(e for e in l)
    e=st.startswith(str1)
    if e==True:
        print("It's a pi song.")
    else:
        print("It's not a pi song.")
