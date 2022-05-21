def pal(x):
    rev=0
    temp=x
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==x:
        return True
    else:
        return False
def rev(x):
    temp=x
    reve=0
    while temp:
        reve=reve*10+temp%10
        temp//=10
    return reve
x=int(input())
x+=rev(x)
while pal(x)==0:
    x+=rev(x)
print(x)