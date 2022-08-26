n=int(input())
a=list(map(int,input().split()))
print(*a,end=' ')
if n%2!=0:
    print("0")