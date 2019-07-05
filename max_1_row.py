#Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s
def index_max_1(m,n):
  g_mat= [1]*(m)
  for i in range(n):
    g_mat[i]=[1]*(n)
  for i in range(m):
    for j in range(n):
      g_mat[i][j]=int(raw_input())
  print(g_mat)
  ones=[]
  for i in range(m):
    count=0
    for j in range(n):
      if(g_mat[i][j]==1):
        count += 1
    ones.append(count)
  return(ones.index(max(ones)))
        
    
print(index_max_1(3,3))
