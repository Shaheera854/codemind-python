s=input()
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j]:
            c+=1
    if c==1:
        print(i)
        break
else:
    print("-1")