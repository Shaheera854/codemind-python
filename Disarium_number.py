n=int(input())
temp=n
i=0
while temp:
    i+=1
    temp//=10
temp=n
s=0
while temp:
    r=temp%10
    s+=r**i
    i-=1
    temp//=10
if s==n:
    print(True)
else:
    print(False)