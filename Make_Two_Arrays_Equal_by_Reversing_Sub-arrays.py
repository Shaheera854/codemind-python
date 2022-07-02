m=int(input())
t=list(map(int,input().split()))
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(n):
        if t[i]==a[j]:
            c=1
            break
    if c==0:
        print(False)
        break
else:
    print(True)