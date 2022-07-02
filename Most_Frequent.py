n=int(input())
a=list(map(int,input().split()))
b=set(a)
max_c=0
k=0
for i in b:
    c=0
    for j in range(n):
       if i==a[j]:
           c+=1
    if max_c<c:
        max_c=c
        k=i
print(k)