def reverse(self):
    ch=""
    for i in self:
        ch=i+ch
        print(ch)
    return ch
S=input("enter a string")
print(reverse(S))