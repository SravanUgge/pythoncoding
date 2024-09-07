def missingnum(self):
    n=len(self)+1
    totalsum=n*(n+1)//2
    actualsum=sum(self)
    missingnumber=totalsum-actualsum
    return missingnumber

numbers= [1,2,3,4,5,6,7,9]
print(missingnum(numbers))