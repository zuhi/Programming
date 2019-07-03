#The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints
#Withdynamic programming
def dy_without_diag(m,n):
  Grid = [1] * m
  for i in range(m):
      Grid[i] = [1] * n
  for i in range(1,m):
    for j in range(1,n):
      if(j!=0 and i!=0):
        Grid[i][j]= Grid[i][j-1]+Grid[i-1][j]
  return(Grid[m-1][n-1])
print("Without_diagonal",dy_without_diag(3,3))
def dy_with_diag(m,n):
  Grid = [1] * m
  for i in range(m):
      Grid[i] = [1] * n
  for i in range(1,m):
    for j in range(1,n):
      if(j!=0 and i!=0):
        Grid[i][j]= Grid[i][j-1]+Grid[i-1][j]+Grid[i-1][j-1]
  return(Grid[m-1][n-1])
print("With_diagonal",dy_with_diag(3,3))
