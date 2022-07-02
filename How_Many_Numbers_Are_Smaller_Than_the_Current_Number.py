n=int(input())
a=list(map(int,input().split()))
for i in a:
    c=0
    for j in a:
        if i>j:
            c+=1
    print(c,end=" ")