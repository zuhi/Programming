#Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value.
from itertools import combinations
def count_(ar,no):
  counter =0
  s=list(combinations(ar,3))
  for i in range(len(s)):
    sum_=0
    for j in range(len(s[i])):
      sum_ += s[i][j]
    if(sum_<no):
      counter = counter+ 1
  return(counter)
print(count_([-2, 0, 1, 3],2))
