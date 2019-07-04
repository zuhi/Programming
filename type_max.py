#Given an array, it can be of 4 types
#(a) Ascending
#(b) Descending
#(c) Ascending Rotated
#(d) Descending Rotated
#Find out which kind of array it is and return the maximum of that array.
ar=[2, 1, 5, 4, 3]
counter=0
counter_d=0
for i in range(len(ar)):

    if(i<len(ar)-1 and i+1<len(ar)):
        if(ar[i]>ar[i+1] ):

          counter = counter+1
        else:
          counter_d += 1
counter= counter+1
counter_d += 1
   
    
if(counter==len(ar)):
  print("descending, max",str(max(ar)))
elif(counter>(len(ar)/2)):
  print("rotated descending",str(max(ar)))
elif(counter_d==len(ar)):
  print("ascending",str(max(ar)))
else:
  print("Rotated descending",str(max(ar)))
