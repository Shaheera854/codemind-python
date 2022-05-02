n=int(input())#76
sqn=pow(n,2)#5776
i=10
r=0
t=0
while r!=sqn:
    r=sqn%i
    if n==r:
        print('Automorphic Number')
        t=1
        break
    i*=10
if t==0:
    print('Not an Automorphic Number')