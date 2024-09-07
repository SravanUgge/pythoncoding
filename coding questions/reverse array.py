A=list(map(int,input("A=").split(",")))
N=int(input("N:"))
def reverse_array(A,N):
    reverse=[]
    for i in range(N-1,-1,-1):
        reverse.append(A[i])
    sum=0
    print(reverse)
    for i in range(N):
        if i%2==0:
            sum+=reverse[i]

    return sum

print(reverse_array(A,N))