#Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]
array=[1, 1, 2, 2, 2, 2, 3]
def count_search(a,number):
  counter=0
  for no in a :
    if(no==number):
      counter += 1
  return(counter)
print("Count",count_search(array,2))
