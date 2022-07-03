s=input()
c=0
c_r=0
c_l=0
for i in range(len(s)):
    if c_r!=0 and c_l!=0 and c_r==c_l:
        c+=1
        c_r=0
        c_l=0
    if s[i]=='R':
        c_r+=1
    if s[i]=='L':
        c_l+=1
print(c+1)