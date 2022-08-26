n=input()
s_min=0
s_max=0
mini=ord(n[0])
maxi=ord(n[0])
for j in range(1,len(n)):
    if mini>ord(n[j]) and n[j].isalnum():
        mini=ord(n[j])
    if maxi<ord(n[j]) and n[j].isalnum():
        maxi=ord(n[j])
print(chr(mini),n.count(chr(mini)),chr(maxi),n.count(chr(maxi)))