s=input()
l=len(s)
c=1
count=0
for i in range(0,l-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        if count<c:
            count=c
        c=1
if count<c:
    count=c
print(count)