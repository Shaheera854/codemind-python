def isprime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
n=int(input())
t=0
for i in range(1,(n//2)+1):
    for j in range(i+1,(n//2)+1):
        if i*j==n and isprime(i) and isprime(j):
            print(i,j)
            t=1
            break
    if t==1:
        break
else:
    print("-1")