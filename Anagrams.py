s1=input().lower()
s2=input().lower()
s1,s2=set(s1),set(s2)
s1,s2=list(s1),list(s2)
s1.sort(),s2.sort()
if s1==s2:
    print(True)
else:
    print(False)