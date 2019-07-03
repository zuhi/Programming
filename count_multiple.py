#Given an unsorted integer (positive values only) array of size ‘n’, we can form a group of two or three, the group should be such that the sum of all elements in that group is a multiple of 3.
#Count all possible number of groups that can be generated in this way
import itertools
array=[3, 6, 7, 2, 9]
lis_= list(itertools.combinations(array,2))
lis_ += list(itertools.combinations(array,3))
count=0
for i in lis_:
  sum_=0
  for j in range(len(i)):
    sum_+= i[j]
  if(sum_%3==0):
    count += 1
print(count)
