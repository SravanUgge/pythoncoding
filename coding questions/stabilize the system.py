num=int(input(":"))
def stablize(num):
    value=str(num)
    newval=""
    for i in range(len(value)):
        if value[i]=='0':
            newval+='5'
        else:
            newval+=value[i]

    return int(newval)
print(stablize(num))