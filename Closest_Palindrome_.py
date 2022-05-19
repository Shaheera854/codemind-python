n=int(input())
for i in range(n-1,n-1000,-1):
    temp=i
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if i==rev:
        d1=n-i
        cp1=i
        break
for i in range(n+1,n+1000):
    temp=i
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if i==rev:
        d2=i-n
        cp2=i
        break
if d1<d2:
    print(cp1)
elif d2<d1:
    print(cp2)
else:
    print(cp1,cp2)