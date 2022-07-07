def is_pal(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if n==rev:
        return True
    return False
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
while True:
    n+=1
    if is_pal(n) and is_prime(n):
        print(n)
        break