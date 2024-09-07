def intersection(self1,self2):
    value=[]
    for i in self1:
        if i in self2:
            value.append(i)
            self2.remove(i)
    return value


arr1=[1,2,2,1]
arr2=[2,2]
print(intersection(arr1,arr2))
