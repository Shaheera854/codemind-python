vowels1=['a','e','i','o','u']
vowels2=['A','E','I','O','U']
t1=0
s=input()
for i in range(5):
    if vowels1[i] not in s:
        t1=1
        break
else:
    print(True)
    exit()
for i in range(5):
    if vowels2[i] not in s:
        print(False)
        break
else:
    print(True)