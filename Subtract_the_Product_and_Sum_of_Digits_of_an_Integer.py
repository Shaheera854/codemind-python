n=int(input())
temp=n
p=1
s=0
while temp:
    r=temp%10
    temp//=10
    p*=r
    s+=r
print(p-s)