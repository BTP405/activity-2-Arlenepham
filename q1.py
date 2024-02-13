# this helper function checks if the integer in the parameter is a prime number. 
# It iterates through the loop, if it diviable for any index, it is not a prime number
def isPrime(n):
    prime = True
    for i in range(2, n):
        if (n % i) == 0:
            prime = False
            break
    return prime

def getPrimeNumbers(n):
    return [i for i in range(2, n) if isPrime(i)] # this list comprehension return a list of int from 2 to n is a prime number

# example
print(getPrimeNumbers(30))
