n=int(input())
sq=n*n
temp=0
i=1
while sq:
    if temp==n:
        print("Automorphic Number")
        break
    temp=(sq%10)*i+temp
    sq//=10
    i*=10
else:
    print("Not an Automorphic Number")