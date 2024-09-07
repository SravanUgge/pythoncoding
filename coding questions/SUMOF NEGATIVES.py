num=list(map(int,input("number:").split()))
def sumofnef(num):
    sum=0
    for n in num:
        if n<0:
            sum+=n
    return sum
print(sumofnef(num))
