#You are given a list of n-1 integers and these integers are in the range of 1 to n.
#There are no duplicates in the list.
#One of the integers is missing in the list. Write an efficient code to find the missing integer
ar=[ 1, 2, 4, 5, 6 ]
def missing_(a):
  print("l",l)
  for i in range(1,l+2):
    if(i not in a):
      return(i)
print(missing_(ar))
