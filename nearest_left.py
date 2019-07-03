#Find the nearest smaller numbers on left side in an array
array=[1, 3, 0, 2, 5]
n_list=['_']*len(array)
for i in range(1,len(array)):
  for j in range(0,i):
    if(array[i]>array[j]):
      n_list[i]=array[j]
print(n_list)
