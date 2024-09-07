a=list(map(int,input(":").split(",")))
n=len(a)
def hike(a,n):
    sorta=sorted(a)
    max=0
    for i in range(n):
        if sorta[i]>=max:
            max=sorta[i]
    return max
print(hike(a,n))