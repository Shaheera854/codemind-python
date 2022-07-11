def palin(i):
    m=0
    while i:
        m=m*10+i%10
        i=i//10
    return m
x = int(input())
l = list(map(int,input().split()))
c=0
for i in l:
    print(palin(i),end=' ')