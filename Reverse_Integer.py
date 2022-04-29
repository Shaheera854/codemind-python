n=int(input())
r=0
m=abs(n)
while m:
    r=r*10+m%10 
    m//=10
if n<0:
    print(-r)
else:
    print(r)