arr=list(map(int,input().split()))
arr2=sorted(arr)
def fun(arr):
    res=""
    for i in range(len(arr)):
        if arr[i]==arr2[0]:
            res+=str(i+1)+" "
    for j in range(len(arr)):
        if arr[j]==arr2[-1]:
            res+=str(j+1)
    return res
print(fun(arr))