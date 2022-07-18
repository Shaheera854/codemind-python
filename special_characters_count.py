s=input()
c=0
for i in s:
    j=ord(i)
    if (j>32 and j<=47) or (j>=58 and j<=64) or (j>=91 and j<=96) or (j>=123 and j<=126):
        c+=1
print(c)