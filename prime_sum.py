#Given an even number (greater than 2 ), 
#print two prime numbers whose sum will be equal to given number.
#There may be several combinations possible. Print only first such pair.
def get_sum(n):
  primes=list()
  for i in range(2,n+1):
    count=0
    for j in range(2,n):
      if(i%j==0 and i!=j):
        count += 1
    if(count==0):
       primes.append(i)
  for i in primes:
    for j in primes:
      if(i+j==n):
        return(i,j)
  return(-1)
get_sum(34)
