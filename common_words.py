s1=input()
s1=str.lower(s1)
s2=input()
s2=str.lower(s2)
s1=s1.split()
s2=s2.split()
for i in s2:
    if i in s1:
        print(i,end=' ')