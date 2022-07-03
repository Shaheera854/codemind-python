s=input()
vowels='aeiou'
c=0
maxi=0
for i in range(len(s)):
    if s[i] in vowels:
        c+=1
        maxi=max(maxi,c)
    else:
        c=0
print(maxi)