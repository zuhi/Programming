#Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x.
#Write efficient functions to find floor of x
def floor_array(n,x):
  n= sorted(n, reverse=True)
  for i in n:
    if(i<x or i==x):
      return(i)
   
  return(-1)

print(floor_array([1, 2, 8, 10, 10, 12, 19],0))
