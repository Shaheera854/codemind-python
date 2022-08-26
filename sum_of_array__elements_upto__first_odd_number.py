n=int(input())
a=list(map(int,input().split()))
i=0
s=0
while i<n:
   if a[i]%2!=0:
       break
   s+=a[i]
   i+=1
print(s)