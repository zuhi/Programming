#Given an array arr[] and a position in array, k.
#Write a function name reverse (a[], k) such that it reverses subarray arr[0..k-1]
def rev(a,pos):
  a_rev=a[0:pos]
  a_rev=a_rev[::-1]
  return(a_rev+a[pos:len(a)])
print(rev([1, 2, 3, 4, 5, 6],4))
