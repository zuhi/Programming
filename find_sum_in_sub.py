#Index of subarray having the same as input number
def find_sum_in(ar,no):
  for i in range(len(ar)):
    currn_sum=0
    for j in range(i,len(ar)):
      currn_sum += ar[j]

      if(currn_sum == no):
        return(i,j)
  return(0)
print(find_sum_in([1, 4, 20, 3, 10, 5],33))
