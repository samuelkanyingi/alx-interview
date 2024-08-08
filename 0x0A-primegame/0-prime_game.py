#!/usr/bin/python3
def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    # Determine the maximum number in nums to set sieve range
    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_num + 1, i):
                is_prime[j] = False

    # Precompute number of primes up to each index
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
