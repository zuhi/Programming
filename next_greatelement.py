#Given an array, print the Next Greater Element (NGE) for every element.
#The Next greater Element for an element x is the first greater element on the right side of x in array.
#Elements for which no greater element exist, consider next greater element as -1
array=[11, 13, 21, 3]
def next_greatElement(a):
  print(a)
  n_list=[0]*len(a)
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      if(a[j]>a[i]):
           n_list[i]=a[j]
           break
      else:
           n_list[i]=-1
  n_list[len(a)-1]=-1
  return(n_list)
print(next_greatElement(array))
