#Find k numbers with most occurrences in the given array
def array_(a):
  d= dict()

  for j in a:
    if(j in d):
      count=d[j]
      d[j]= count+1
    else:
      d[j]=1
  
  return(d)
ar= (array_([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]))
count=0
print(ar)
for key,value in(sorted(ar.items(), key=lambda x: x[1], reverse=True)):
    if(count<=3):
       print(key)
       count += 1
    else:
       break
