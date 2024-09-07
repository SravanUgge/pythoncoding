word=input("word")
n=int(input("length of the word"))
c=input("char to count:")
def charcount(word,n,c):
    count=0
    for i in range(n):
        if word[i]==c:
            count+=1
    return count
print(charcount(word,n,c))
