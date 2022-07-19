def pal(s):
    if s[::-1]==s:
        return True
    else:
        return False
s=input()
s=str.lower(s)
s=s.split()
c=0
for i in s:
    if pal(i):
        c+=1
print(c)