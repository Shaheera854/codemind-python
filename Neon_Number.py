n=int(input())
sq=pow(n,2)
s=0
while sq:
    r=sq%10
    sq//=10
    s+=r
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')