a=100
def magic(a):
    count=0
    for k in range(1,a):
        b=bin(k)[2:]
        str=""
        for i in range(len(b)):
            if b[i]=="0":
                str+="1"
            elif b[i]=="1":
                str+="2"
        sum=0
        for j in str:
            sum+=int(j)
        if sum%2!=0:
            count+=1
    return count
print(magic(a))
