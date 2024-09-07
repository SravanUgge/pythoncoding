s=input()
ch1=input()
ch2=input()
def mismatch(s,ch1,ch2):
    word=""
    for i in range(len(s)):
        if s[i]==ch1:
            word+=ch2
        #elif s[i]==ch2:
         #   word+=ch1
        else:
            word+=s[i]
    return word
print(mismatch(s,ch1,ch2))