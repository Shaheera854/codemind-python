n,x=map(int,input().split())
i=1
k=0
temp=n
while temp:
    temp//=10
    k+=1
j=10**(k-1)
c=10
while i<=x:
    f=n//j
    l=n%c
    i+=1
    j//=10
    c*=10
print(abs(f-l))