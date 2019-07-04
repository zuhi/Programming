#Given a sorted array with possibly duplicate elements,
#the task is to find indexes of first and last occurrences of an element x in the given array
ar=[1, 3, 5, 5, 5, 5 ,67, 123, 125]
def first_last(a,chck):
  d= dict()
  for i in a:
    if(i not in d):
      d[i]=1
    else:
      d[i]=d[i]+1
  for i in range(len(a)):
    if(a[i]==chck):
      return(i,i+(d[a[i]]-1))
print(first_last(ar,5))
