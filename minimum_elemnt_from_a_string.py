s=input().split()
s=s[len(s)-1]
s1=''
for i in s:
    if str.isalpha(i):
        s1+=i
m=min(s1)
if str.isupper(m) and str.lower(m) in s1:
    print(str.lower(m))
else:
    print(m)