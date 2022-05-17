def power(n):#n=9
    a,b=0,1
    i=0
    while True:
        c=2**i#c=16
        a=b
        b=c
        if b>n:#16>9
            d1=b-n#d1=16-9=7
            d2=n-a#d2=9-8=1
            break
        i+=1#i=4
    if d1<d2:
        return d1
    else:
        return d2
n=int(input())
print(power(n))