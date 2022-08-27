s=input().lower()
a=[]
vowels='aeiou'
for i in vowels:
    if i not in s:
        a.append(i)
if len(a)==0:
    print("0")
else:
    print(*sorted(a))