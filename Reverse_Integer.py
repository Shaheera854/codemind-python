n=int(input())
temp=abs(n)
rev=0
while temp:
    rev=rev*10+temp%10
    temp//=10
if n>0:
    print(rev)
else:
    print("-{}".format(rev))