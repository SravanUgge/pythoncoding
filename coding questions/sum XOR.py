A=list(map(int,input("array:").split(",")))
N=int(input("enter the length:"))
def SUMXOR(A,N):
    result=0
    sum=0
    for i in range(N):
        if i%2==0:
            result=result^A[i]
        else:
            sum+=A[i]
    return sum-result
print(SUMXOR(A,N))

