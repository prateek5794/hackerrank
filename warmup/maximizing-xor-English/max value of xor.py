#!/usr/bin/python3
def maxXor(l, r):
    list=[]
    for w in range (l,r+1):
        l=w
        for k in range(w,r+1):
            list.append(w^k)
            a=w^k
            print("{0} xor {1}={2}".format(w,k,a))
    h=max(list)
    print(list)
    return h
if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))
