#Given two sorted arrays such the arrays may have some common elements.
#Find the sum of the maximum sum path to reach from beginning of any array to end of any of the two arrays.
#We can switch from one array to another array only at common elements.
#Note that the common elements do not have to be at same indexes
def constrain_check(a1,a2):
  m= len(a1)
  n= len(a2)
  i=0
  j=0
  sum1=0
  sum2=0
  result=0
  while(i<m and j<n):
    if(a1[i]>a2[j]):
      sum2 += a2[j]
      j += 1
    elif(a1[i]<a2[j]):
      sum1 += a1[i]
      i +=1
    else:
      result += max(sum1,sum2)
      sum1= 0
      sum2= 0
      while(i<m and j<n and a1[i]==a2[j]):
        result += a1[i]
        i += 1
        j += 1
  while(i<m):
    sum1 += a1[i]
    i += 1
  while(j<n):
    sum2 += a2[j]
    j += 1
  result += max(sum1,sum2)
  return(result)

print(constrain_check([2, 3, 7, 10, 12, 15, 30, 34],[1, 5, 7, 8, 10, 15, 16, 19]))
