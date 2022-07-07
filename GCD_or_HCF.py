def hcf(a,b):
    if a>b:
        a,b=b,a
    c=a
    while c>=1:
        if a%c==0 and b%c==0:
            return c
        c-=1
a,b=map(int,input().split())
print(hcf(a,b))