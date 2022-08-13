n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
    if i in a:
        a.remove(i)
    elif i not in a:
        print("No")
        break
else:
    print("Yes")