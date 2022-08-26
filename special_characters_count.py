s=input()
c=0
for i in s:
   if i.isalnum() or i==' ':
       continue
   else:
       c+=1
print(c)