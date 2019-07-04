#Given an unsorted array that may contain duplicates. Also given a number k which is smaller than size of array.
#Write a function that returns true if array contains duplicates within k distance
def dup_ink(a,k):
  check_=a[0:k]
  if(len(check_)==len(set(check_))):
    return False
  else:
    return True
print(dup_ink([1, 2, 3, 4, 1, 2, 3, 4],7))
