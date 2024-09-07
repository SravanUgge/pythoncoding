def duplicate(self):
    final=[]
    for i in self:
        if self[i]==self[i+1]:
            final.remove(i)
    return final
array=[1,22,22,3,4,5]
print(duplicate(array))