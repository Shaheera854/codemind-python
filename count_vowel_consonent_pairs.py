s=input()
c=0
v='AEIOUaeiou'
co='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
x=0
y=len(s)-1
while x<y:
    if ((s[x] in v and s[y] in co) or (s[x] in co and s[y] in v)):
        c+=1
    x+=1
    y-=1
print(c)