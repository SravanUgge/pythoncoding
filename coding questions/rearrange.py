def rearrange():
    s=input().strip()
    t=input().strip()
    arr1=sorted(s)
    arr2 =sorted(t)
    if arr1 == arr2 :
        return True
    else:
        return False
print(rearrange())