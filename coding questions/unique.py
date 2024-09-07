def unique(arr):
    uniqueelement=[]
    for elem in arr:
        if elem not in uniqueelement:
            uniqueelement.append(elem)
    return uniqueelement
arr=[1,2,2,3,4,4,5]
print(unique(arr))

