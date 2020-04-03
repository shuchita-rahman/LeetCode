def countPrimes(self, n: int) -> int:
  isprime = [True] * n
  primeCount = 0
 
 for i in range(2, n):
      if isprime[i] == True:
          primeCount = primeCount +1
          for j in range(i*i, n, i):
              isprime[j] = False
  return primeCount 
            
        
        
