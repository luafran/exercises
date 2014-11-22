import sys


def calc_primes(max_prime):

    primes = [2]
    
    current = 3
    while current <= max_prime:
        for prime in primes:
            if current % prime == 0:
                break
        else:
            primes.append(current)
        current += 2

    print repr(primes)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage:", sys.argv[0], "limit"
        raise SystemExit
    limit = int(sys.argv[1])

    calc_primes(limit)