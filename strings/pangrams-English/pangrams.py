s=input().lower()
g=0
for k in range(97,123):
    try:
        s.index(chr(k))
    except ValueError:
        g=-1
if g==-1:
    print('not pangram')
else:
    print('pangram')
