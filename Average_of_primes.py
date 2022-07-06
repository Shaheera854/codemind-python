def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    if is_prime(a[i]):
        s+=a[i]
        c+=1
print("{:.2f}".format(s/c))