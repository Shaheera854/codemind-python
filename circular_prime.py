def reverse(num):
    rev=0
    temp=num
    while temp:
        rev=rev*10+temp%10
        temp//=10
    return rev
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if is_prime(n):
    rev=reverse(n)
    if is_prime(rev):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
