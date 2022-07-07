n=int(input())
sq=n*n
s=0
while sq:
    r=sq%10
    sq//=10
    s+=r
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")