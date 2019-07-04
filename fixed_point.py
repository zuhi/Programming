#Find a Fixed Point (Value equal to index) in a given array
ar=[-10, -5, 0, 3, 7]
def check_index_value(a):
  for i in range(len(a)):
    if(i==a[i]):
      return(i)
  return(-1)
print(check_index_value(ar))
