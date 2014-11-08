
if __name__ == "__main__":
    
    max = 50
    primes = [2]
    
    current = 3
    while current <= max:
        for prime in primes:
            if current % prime == 0:
                break
        else:
            primes.append(current)
        current = current + 2

    print repr(primes)
