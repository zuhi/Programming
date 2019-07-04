#Given an unsorted array, find the minimum difference between any pair in given array
from itertools import combinations
ar=[30, 5, 20, 9]
def min_diff(a):
  min_=9999
  comb= list(combinations(a,2))
  for i in comb:
    min_v= abs(i[0]-i[1])
    if(min_v<min_):
      min_=min_v
  return(min_)
print(min_diff(ar))
