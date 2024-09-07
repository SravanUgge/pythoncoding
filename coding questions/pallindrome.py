string=str(input(":"))
def pallindrome(self):
    str2=""
    for i in range(len(self)):
        str2=self[i]+str2


    if self == str2:
        return True
    else:
        return  False
print(pallindrome(string))