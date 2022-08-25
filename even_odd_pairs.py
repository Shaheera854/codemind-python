n=int(input())
l=list(map(int,input().split()))
l_e=[]
l_o=[]
for i in range(n):
    if l[i]%2==0:
        l_e.append(l[i])
    else:
        l_o.append(l[i])
i=0
j=0
while  i<len(l_e) or j<len(l_o):
    if i<len(l_e):
        print(l_e[i],end=' ')
        i+=1
    if j<len(l_o):
        print(l_o[j],end=' ')
        j+=1
if n%2!=0:
    print("0")