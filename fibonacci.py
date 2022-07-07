n=int(input())
print(0,1,end=" ")
a,b=0,1
for i in range(2,n):
    c=a+b
    print(c,end=' ')
    a,b=b,c