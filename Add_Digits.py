n=int(input())
sum=0
while n:
    sum+=n%10
    n//=10
    if n==0 and sum>9:
        n=sum
        sum=0
print(sum)
