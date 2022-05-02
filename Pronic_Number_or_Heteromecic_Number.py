n=int(input())
t=0
for i in range(1,n//2):
    if i*(i+1)==n:
        print('YES')
        t=1
        break
if t==0:
    print('NO')
        