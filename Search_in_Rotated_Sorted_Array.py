n=int(input())
a=list(map(int,input().split()))
t=int(input())
for i in range(n):
    if a[i]==t:
        print(i)
        break
else:
    print("-1")