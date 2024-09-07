a=list(map(int,input().split(",")))
n=len(a)
def fin(a,n):
    count=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            count+=1
    return count
print(fin(a,n))
