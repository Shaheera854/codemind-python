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
for i in range(n):
    if is_prime(a[i]):
        c+=1
print(c)