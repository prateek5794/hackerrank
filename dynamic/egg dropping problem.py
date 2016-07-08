import sys
f=100
n=2
m=[[k for k in range(1,f+1)] for k in range(n)] # initialising 2*100 matrix
for i in range(1,n): #loop start from 2nd row, row indicate no of eggs
    for j in range(f):
        mi=sys.maxsize
        for k in range(j+1):
            if j<i: #if no of eggs are less than floor copy the upper row element
                m[i][j]=m[i-1][j]
                continue
            elif k==0: #if egg is dropped from 1st floor the egg will breake and we will get answer
                q=m[i][j-1] #or the egg will remain same and no. of floor will decrease
            elif k==j: #if egg is dropped from last floor either we will get answer
                q=m[i-1][j-1] # or egg will break, so we will left with one less egg and 1 less floor
            else: #if egg broke than 1 less egg and floor below the floor from we dropped the egg
                q=max(m[i-1][k-1],m[i][j-k-1]) #if egg doesn't break than floor above and same number of egg
            if q<mi:
                mi=q
            m[i][j]=1+mi
print(m)
