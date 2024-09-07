n=int(input(":"))
def prime(n):
    primes=[]
    sum=0
    if (n==0) or (n==1):
        primes.append(0)

    for num in range(2,n+1):
        for i in range(2,num):
            if (num%i)==0:
               break
        else:
            primes.append(num)
    for j in range(len(primes)):
        sum+=primes[j]
    return sum

print(prime(n))