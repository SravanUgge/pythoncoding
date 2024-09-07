N=int(input("enter the length of the array:"))
A=list(map(int,input("enter list:").split(",")))
def maxpair(A,N):
    max=[]
    sortval=sorted(A)
    new=0
    for i in range(0,N-1):
        for j in range(1,N):
            if A[i]+A[j]==18:
                temp=A[i]*A[j]
                if temp>=new:
                    new=temp
                    max=[A[i],A[j]]
    return max
print(maxpair(A,N))
