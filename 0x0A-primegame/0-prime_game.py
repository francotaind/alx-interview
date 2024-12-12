#!/usr/bin/python3

def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if x <= 0 or not nums:
        return None

    # Helper function to generate a list of primes up to n using Sieve of Eratosthenes
    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    # Precompute primes for the largest n in nums
    max_n = max(nums)
    primes = sieve(max_n)

    # Count cumulative primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if prime_count[n] % 2 == 1:  # Maria wins if the number of primes is odd
            maria_wins += 1
        else:  # Ben wins if the number of primes is even
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
