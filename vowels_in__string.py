vowels=['a','e','i','o','u','A','E','I','O','U']
s=input()
d=[]
for i in s:
    if i in vowels and i not in d:
        d.append(i)
if len(d)==0:
    print('-1')
else:
    print(*d)