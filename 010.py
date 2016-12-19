import math

def isPrime(n):
  if n == 2:
      return True
  if n < 2 or n % 2 == 0:
      return False;
  max = int(math.sqrt(n));
  for i in range(3, max+1, 2):
      if n % i == 0:
          return False
  return True


def primeGenerator(n):
    """Generates prime numbers < n"""
    primes = [2]
    if n > 2:
        candidates = [c for c in range(3, n, 2)]
        for test in range(3, int(math.sqrt(n))+1, 2):
            for c in candidates:
                if c > test and c % test == 0:
                    candidates.remove(c)
        primes += candidates
    return primes

if __name__ == '__main__':
    primes = primeGenerator(2000000)
    print sum(primes)
