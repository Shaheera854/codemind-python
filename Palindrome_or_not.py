def pal(s):
    if s[::-1]==s:
        return True
    return False
s=input()
s=str.lower(s)
print(pal(s))