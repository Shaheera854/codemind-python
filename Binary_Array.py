n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i!=0 and i!=1:
        print(False)
        break
else:
    print(True)