h=int(input())
m=int(input())
s=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one", "twenty two", "twenty three", "twenty four", "twenty five","twenty six","twenty seven","twenty eight","twenty nine"]
if m>30:
    if m==45:
        print('quarter to '+s[h+1])
    elif m==59:
        print('one minute to '+s[h+1])
    else:
        print(s[60-m]+' minutes to '+s[h+1])
elif m<30:
    if m==0:
        print(s[h]+" o' clock" )
    elif m==15:
        print('quarter past '+s[h])
    elif m==1:
        print('one minute past '+s[h])
    else:
        print(s[m]+' minutes past '+s[h])
elif m==30:
    print('half past '+s[h])
