#Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
array=[1,2,3,4,5,6,7] 
def rotate_by(a,d):
  return(a[d:len(a)]+a[0:d])

print(rotate_by(array,2))
