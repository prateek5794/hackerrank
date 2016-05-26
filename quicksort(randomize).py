import random
def par(l,p,r):
    w=random.randint(p,r)
    x=l[w]
    l[w],l[r]=l[r],l[w]
    p-=1
    r+=1
    while(True):
        while(True):
            p+=1
            if(l[p]>=x):
                break
        while(True):
            r=r-1
            if(l[r]<=x):
                break
        if p<r:
            l[p],l[r]=l[r],l[p]
        elif p==r:
            r-=1
            return r
        else:
            return r

def quicksort(l,p,r):
    if (p<r):
        q=par(l,p,r)
        quicksort(l,p,q)
        quicksort(l,q+1,r)
    else:
        return
l=list(map(int,input().split()))
quicksort(l,0,len(l)-1)
print(l)
