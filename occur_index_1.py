#Index of ocurrence of first 1
ar=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
def first_1(a):
  for i in range(len(a)):
    if(a[i]==1):
      return(i)
print(first_1(ar))
