n=int(input())
a=list(map(int,input().split()))
b=sorted(a)[::-1]
if a==b:
    print("yes")
else:
    print("no")