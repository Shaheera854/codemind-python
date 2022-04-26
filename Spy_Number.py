n=int(input())
s=0
p=1
while n:
    r=n%10
    n//=10
    s+=r
    p*=r
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')