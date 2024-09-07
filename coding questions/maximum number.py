def maximum(self):
    max=self[0]
    for i in self:
        if i > max:
            max=i
    return max
array=[345,56343,23,7567,325,678973]
print(maximum(array))


