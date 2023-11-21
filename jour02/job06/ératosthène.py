# Programme pour afficher les nombres premiers jusqu'à 1000

def crible_eratosthene(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for current_number in range(2, int(limit**0.5) + 1):
        if sieve[current_number]:
            primes.append(current_number)
            for multiple in range(current_number * current_number, limit + 1, current_number):
                sieve[multiple] = False

    for remaining_number in range(int(limit**0.5) + 1, limit + 1):
        if sieve[remaining_number]:
            primes.append(remaining_number)

    return primes

# Afficher les nombres premiers jusqu'à 1000
limit = 1000
resultat = crible_eratosthene(limit)
print(resultat)