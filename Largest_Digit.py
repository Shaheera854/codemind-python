n=int(input())
maxi=0
while n:
    r=n%10
    maxi=max(maxi,r)
    n//=10
print(maxi)