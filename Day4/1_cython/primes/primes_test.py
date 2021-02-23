import primes
import cy_primes

%timeit primes.primes(2000)

%timeit cy_primes.primes(2000)