s=input()
vowels='aeiouAEIOU'
l=[]
for i in s:
    if i in vowels and i not in l:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(*l)