import csv
while(True):
    n=input()
    if(int(n)==-1):
        break
    ifile  = open('sites.csv', "r")
    reader = csv.reader(ifile)
    for row in reader:
        if(row[0]==n):
            k=row[1]
            j=row[0]
    ifile.close()
    ifile  = open('ads.csv', "r")
    reader = csv.reader(ifile)
    l=[]
    m=0
    for row in reader:
        row=list(x.strip() for x in row)
        if(m==0):
            m+=1
        elif(int(row[1])>=int(k) and (j in row[2:])):
            l.append([row[1],row[0],row[2]])
    ifile.close()
    if(len(l)==0):
        print("0 0")
    elif(len(l)==1):
        print(l[0][1],k)
    else:
        l.sort()
        if(l[0][0]==l[1][0]):
            if(l[0][2]>=l[1][2]):
                print(l[0][1],l[0][0])
            else:
                print(l[1][1],l[0][0])
        else:
            print(l[0][1],l[1][0])
