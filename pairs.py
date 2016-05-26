#!/usr/bin/py
# Head ends here
def pairs(a,k):
    j=0
    for g in range(len(a)):
        for l in range(g+1,len(a)):
            if abs(a[g]-a[l])==k:
                j+=1
    return j
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
