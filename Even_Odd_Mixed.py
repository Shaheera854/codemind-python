n=int(input())
c=0
ce=0
co=0
while n:
    r=n%10
    n//=10
    c+=1
    if r%2==0:
        ce+=1
    if r%2!=0:
        co+=1
if c==ce:
    print("Even")
elif c==co:
    print("Odd")
else:
    print("Mixed")