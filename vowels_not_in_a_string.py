s=input()
vowels=['a','e','i','o','u']
l=[]
for i in vowels:
    if i not in s:
        l.append(i)
if len(l)==0:
    print('0')
else:
    print(*l)