def reverse(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    return rev
n=int(input())
sq_n=n*n
sq_r=(reverse(n))**2
if sq_n==reverse(sq_r):
    print(True)
else:
    print(False)