#!/bin/python3

import sys

# Complete the function below.


def  swap_array( a):
    ones=[]
    f=[]
    for i in a:
        binary = bin(i)[2:]
        k=binary.count('1')
        ones.append([k,i])
    j=0
    ones.sort()
    while(j<len(ones)):
        h=j
        if(j<len(ones)-1):
            while(ones[j][0]==ones[j+1][0]):
                j+=1
        k=j
        j+=1
        while(k>h-1):
            f.append(ones[k][1])
            k-=1
    for p in f:
        print(p,end='\n')
            
_a_cnt = 0
_a_cnt = int(input())
_a_i=0
_a = []
while _a_i < _a_cnt:
    _a_item = int(input());
    _a.append(_a_item)
    _a_i+=1
    

swap_array(_a);

