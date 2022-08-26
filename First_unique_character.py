s=input()
s=s.lower()
l=0
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j] and s[i]!=' ':
            c+=1
    if c==1:
        print(s[i])
        break
else:
    print("-1")