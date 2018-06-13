limit = 100

def primeGen(limit):
    table = [True] * limit
    for i in range(2,limit):
        if table[i]:
            j = 2
            while True:
                non_prime = i * j
                j += 1
                if non_prime >= limit:
                    break
                else:
                    table[non_prime] = False
            yield i

primes = primeGen(limit)
for prime in primes:
    print(prime)


