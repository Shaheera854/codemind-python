n=int(input())
i=1
s=0
while i<=n//2:
    if n%i==0:
        s+=i
    i+=1
if s==n:
    print('True')
else:
    print('False')