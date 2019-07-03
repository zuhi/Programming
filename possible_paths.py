#The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints
#recursion
def rec_count_with_diagonals(m,n):
  print("m,n",m,n)
  if(m==3 or n==3):
    return(1)

  return rec_count(m+1, n)+rec_count(m,n+1)+rec_count(m+1,n+1)
def rec_count_without_diagonals(m,n):
  print("m,n",m,n)
  if(m==3 or n==3):
    return(1)

  return rec_count(m+1, n)+rec_count(m,n+1)
print("possible path without diagonals",rec_count_without_diagonals(1,1))
print("possible path with diagonals",rec_count_with_diagonals(1,1))
