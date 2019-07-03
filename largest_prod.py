#Given an array consisting of n positive integers, and an integer k.
#Find the largest product subarray of size k, i.e., find maximum produce of k contiguous elements in the array where k <= 
import itertools
#array=[6, -3, -10, 0, 2]
array=[1, 5, 9, 8, 2, 4,
                 1, 8, 1, 2]
l=[]
mult=[]
for i in range(2,len(array)):
  l += list(itertools.combinations(array,i))
print(l)
for i in range(len(l)):
  p=1
  for j in l[i]:
    p *= j
  mult.append(p)
print("max",max(mult))
