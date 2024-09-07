#anagrm=both strings have same lenght and the words can be formed together to form a new word

s1=input("s1:")
s2=input("s2:")
def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    elif sorted(s1)==sorted(s2):
        return True
    else:
        return False


print(anagram(s1,s2))