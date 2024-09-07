arr=list[map(int,input().split())]
print(arr)
n=len(arr)
def productpair(arr,n):
    x=set()
    for i in range(n):
        for j in range(i+1,n):
            if ((arr[i]*arr[j]) % 3) == 0:
                x.add(tuple((arr[i],arr[j])))
    return (len(x)+1)

print(productpair(arr,n))