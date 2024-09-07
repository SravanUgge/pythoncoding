a=list(map(int,input().split()))
n=len(a)
def evenodd(a,n):
    res=""
    for i in range(n):
        if a[i]%2==0:
            res+="even "
        else:
            res+="odd "
    return res
print(evenodd(a,n))