n=int(input())
a=list(map(int,input().split()))
a_e=[]
a_o=[]
for i in a:
    if i%2==0:
        a_e.append(i)
    else:
        a_o.append(i)
print(*a_e,end=' ')
print(*a_o)