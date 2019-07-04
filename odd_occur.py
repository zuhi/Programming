#Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times.
ar=[1, 2, 3, 2, 3, 1, 3]
def odd_occ_no(a):
  d=dict()
  for i in a:
    if(i not in d):
      d[i]=1
    else:
      d[i] += 1
  for key, value in d.items():
    if(value%2!=0):
      return(key)
print(odd_occ_no(ar))
