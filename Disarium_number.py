n=int(input())
temp=n
c=0
while temp:
    c+=1
    temp//=10
temp=n
s=0
while temp:
    r=temp%10
    temp//=10
    p=r**c
    s+=p
    c-=1
if n==s:
    print(True)
else:
    print(False)