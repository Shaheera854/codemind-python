s1=input().lower().split()
s2=input().lower().split()
c=0
for i in s1:
    if s1.count(i)==1 and s2.count(i)==1:
        c+=1
print(c)