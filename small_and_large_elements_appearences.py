s=input()
s1=''
c1=0
c2=0
for i in s:
    if str.isalpha(i):
        s1+=i
maxi=max(s1)
mini=min(s1)
for i in s1:
    if maxi==i:
        c1+=1
    if mini==i:
        c2+=1
print(mini,c2,maxi,c1)