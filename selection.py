import random
def par(l,p,r):
    w=random.randint(p,r)
    l[p],l[w]=l[w],l[p]
    i,j=p+1,p+1
    while(j<=r):
        if(l[j]<=l[p]):
            l[i],l[j]=l[j],l[i]
            i+=1
            j+=1
        else:
            j+=1
    l[p],l[i-1]=l[i-1],l[p]
    return i-1
def quicksort(l,p,r,e):
    if (p<r):
        q=par(l,p,r)
        if q==e-1:
            print(l[q])
        elif q>e-1:
            quicksort(l,p,q-1,e)
        else:
            quicksort(l,q+1,r,e-1)
    else:
        return
l=list(map(int,input().split()))
e=int(input())
quicksort(l,0,len(l)-1,e)
print(l)
