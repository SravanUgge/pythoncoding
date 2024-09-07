values=list(map(int,input("enter the values:").split(",")))
def midindex(values):
    for i in values:
        if i<0:
            values.remove(i)
        else:
            sortvalues=sorted(values)
            midvalue=(len(sortvalues)-1)//2

    return sortvalues[midvalue]
print(midindex(values))