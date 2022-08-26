s1=input().lower().split()
s2=input().lower().split()
s2=list(s2)
for i in s2:
    if i in s1 and i!=' ':
        print(i,end=' ')