t=int(input())
assert t<11 and t>0
for _ in range(t):
    k=int(input())
    assert k<=10000000 and k>1
    print(int(k/2)*int(k/2)+int(k/2)*(k%2))
