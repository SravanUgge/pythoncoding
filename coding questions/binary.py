s=input(":")
count=0
res=""
for c in s:
    if c == '0' and count ==0:
        count=0
    elif c == '0' and count > 0:
        res+=chr(ord('A')+count-1)
        count = 0
    else:
        count+=1
if s[len(s)-1]=='1':
    res += chr(ord('A') + count - 1)
print(res)
