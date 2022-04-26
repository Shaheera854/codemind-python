a,b=map(int,input().split())
i=1
if a>b:
    for i in range(1,b+1):
        if (a*i)%b==0:
            print(a*i)
            break
    i+=1
else:
    for i in range(i,a+1):
        if (b*i)%a==0:
            print(b*i)
            break
    i+=1