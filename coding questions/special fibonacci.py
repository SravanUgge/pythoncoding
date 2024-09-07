N=int(input("enter Nth term:"))
def fibo(N):
    if N==0:
        return 0
    if N==1:
        return 1
    else:
        res=[0]*[N+1]
        res[0]=0
        res[1]=1
        for i in range(2,N+1):
            res[i]=(res[i-1]*res[i-1]+res[i-2]*res[i-2])%47
        return  res[N]

print(fibo(N))
