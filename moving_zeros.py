#Given an array of random numbers, Push all the zero’s of a given array to the end of the array.
#For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.
array=[1, 2, 0, 4, 3, 0, 5, 0]
def del_0(a):
  indx=[]
  for i in range(len(a)):
    if(a[i]==0):
      indx.append(i)
  indx=sorted(indx,reverse=True)
  for i in indx:
     a.pop(i)
  for _ in range(len(indx)):
    a.append(0)
  return(a)
print(del_0(array))
