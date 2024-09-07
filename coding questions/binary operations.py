num1=input("num1:")
num2=input("num2:")
operator=input("operator:")
def operation(self1,self2,self3):
    result=""
    if self3 == 'AND':
        for i in range(len(self1)):
            if self1[i] == '1' and self2[i] == '1':
                result+='1'
            else:
                result+='0'
    elif self3 == 'OR':
        for i in range(len(self1)):
            if self1[i] == '1'or self2[i] == '1' :
                result += '1'
            else:
                result += '0'
    elif self3 == 'XOR':
        for i in range(len(self1)):
            if self1[i] == self2[i]:
                result += '1'
            else:
                result += '0'
    return result
print(operation(num1,num2,operator))
