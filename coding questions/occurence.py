def occurence(arr):
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
arr=[1,2,2,3,3,3,4]
print(occurence(arr))