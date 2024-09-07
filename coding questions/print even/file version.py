s=list(input().split())
n=len(s)
def version(s,n):
    file=[]
    new=0
    for i in range(n):
        x=s[i][5:]
        y=int(x)
        file.append(y)
    ver=sorted(file)

    for j in range(n):
        if ver[j]>=new:
            new=ver[j]

    return new
print(version(s,n))
