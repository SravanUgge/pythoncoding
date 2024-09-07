arr=int(input(":"))
def reverse(self):
    digit=""
    for i in range(len(self)):
        digit=self[i]+digit
    return int(digit)

arr2=str(arr)
reversestr=reverse(arr2)
print(reversestr)
