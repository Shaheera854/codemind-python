n=int(input())
while n!=0:
    if n//10==0:
        print(n)
        break
    else:
        s=0
        while n:
            r=n%10
            n//=10
            s+=r
        n=s
            