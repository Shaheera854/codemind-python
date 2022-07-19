s1=input()
s2=input()
s1=str.lower(s1)
s2=str.lower(s2)
s1=s1.split()
s2=s2.split()
i=0
j=0
while i<len(s1):
    j=i+1
    while j<len(s1):
        if s1[i]==s1[j]:
            del s1[j]
            del s1[i]
            i-=1
            break
        j+=1
    i+=1
i=0
j=0
while i<len(s2):
    j=i+1
    while j<len(s2):
        if s2[i]==s2[j]:
            del s2[j]
            del s2[i]
            i-=1
            break
        j+=1
    i+=1
c=0
for i in s1:
    if i in s2:
        c+=1
print(c)