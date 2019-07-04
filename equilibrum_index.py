#Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes
ar=[-7, 1, 5, 2, -4, 3, 0]
def sum_(b):
  sum_count=0
  for i in b:
    sum_count += i
  return(sum_count)
def equi_(a):
  for i in range(1,len(a)-1):
    index=i
    left_sum= sum_(a[0:index])
    right_sum= sum_(a[index+1:len(a)])
    if(left_sum==right_sum):
      return(i)
  return(-1)
print(equi_(ar))
