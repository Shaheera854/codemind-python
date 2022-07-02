n=int(input())
a=list(map(int,input().split()))
t=int(input())
f=-1
l=-1
for i in range(n):
    if a[i]==t and f==-1:
        f=i
    if a[i]==t:
        l=i
print(f,l)