#Given an array of integers, find the length of the longest subarray with sum equals to 0.
def max_seq_0(ar):
  max_len=0
  for i in range(len(ar)):
    curr_sum=0
    for j in range(i,len(ar)):
      curr_sum += ar[j]
      if(curr_sum==0):
        max_len=max(max_len,j-i+1)
  return(max_len)
print(max_seq_0([15, -2, 2, -8, 1, 7, 10, 23]))
