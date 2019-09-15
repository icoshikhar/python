import datetime

def length_primes(num):
    if num < 2:
        return 0
    t1 = datetime.datetime.now()
    primes = [2,3]
    x = 5
    while x <= num:
        for i in range(0, len(primes)):
            if x % primes[i] == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    t2 = datetime.datetime.now()
    
    print(t2 - t1)
    
    return len(primes)
