n=int(input())
a=list(map(int,input().split()))
b=set(a)
if a==sorted(list(b)):
    print("yes")
else:
    print("no")