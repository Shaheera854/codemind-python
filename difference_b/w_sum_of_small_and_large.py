s=input().split()
maxi=0
mini=0
add=0
for i in s:
    maxi+=ord(max(i))
    mini+=ord(min(i))
print(maxi-mini)