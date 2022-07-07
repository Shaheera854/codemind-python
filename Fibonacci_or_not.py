def fibi(n):
    a,b=0,1
    if n==0 or n==1:
        return True
    while True:
        c=a+b
        if c>n:
            return False
        if c==n:
            return True
        a,b=b,c
n=int(input())
print(fibi(n))
