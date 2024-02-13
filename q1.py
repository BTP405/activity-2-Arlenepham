# this helper function checks if the integer in the parameter is a prime number. 
def isPrime(n):
    prime = True
    # if n is divisible by any index, it is not a prime number
    for i in range(2, n):
        if (n % i) == 0:
            prime = False
            break
    return prime

def getPrimeNumbers(n):
    return [i for i in range(2, n) if isPrime(i)] # comprehension to generate list that contains values that makes isPrime = true

# example
print(getPrimeNumbers(30))
