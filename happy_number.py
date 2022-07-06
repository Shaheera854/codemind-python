n=int(input())#32
i=0
while n!=1 and n!=7:
    s=0
    temp=n#temp=1
    while temp:
        r=temp%10#r=1
        s+=r**2#s=0+1=1
        temp//=10
    n=s#n=1
    i+=1
    if i>50:
        break
if n==1 or n==7:
    print(True)
else:
    print(False)
