num=int(input())
l=num%10
num//=10
t=num%10
num//=10
s=num%10
num//=10
f=num%10
if f==6:
    f=9
elif s==6:
    s=9
elif t==6:
    t=9
else:
    l=9
print((((f*10+s)*10+t)*10+l))