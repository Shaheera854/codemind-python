def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
c=0
n=int(input())
a=list(map(int,input().split()))
mini=min(a)
ind_min=a.index(mini)
maxi=max(a)
ind_max=a.index(maxi)
if ind_min>ind_max:
    for i in range(ind_max,ind_min+1):
        if is_prime(a[i]):
            c+=1
else:
    for i in range(ind_min,ind_max+1):
        if is_prime(a[i]):
            c+=1
print(c)