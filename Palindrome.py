def is_pal(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==n:
        return True
    return False
n=int(input())
print(is_pal(n))