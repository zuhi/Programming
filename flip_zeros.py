#Given a binary array and an integer m, find the position of zeroes flipping which creates maximum number of consecutive 1’s in array.
def find_a(ar,m):
  indx=[]
  for i in range(len(ar)):
    if(ar[i]==0):
        indx.append(i)

  d_l=dict()
  d_r= dict()
  for i in range(len(indx)):
    new_ar=ar[0:indx[i]]

    count=0
    for j in range(len(new_ar)-1,-1,-1):
 
      chk=j
      if(new_ar[j]==0):
        break
      elif(new_ar[j]==1 and chk==j):
        count +=1
        chk += 1
      else:
        break
    d_l[indx[i]]=count
  for i in range(len(indx)):
    new_ar=ar[indx[i]+1:len(ar)]

    count=0
    for j in range(len(new_ar)):
  
      chk=j
      if(new_ar[j]==0):
        break
      elif(new_ar[j]==1 and chk==j):
        count +=1
        chk += 1
      else:
        break
    
    d_r[indx[i]]=count
  d_final=dict()
  for (k,v), (k2,v2) in zip(d_r.items(),d_l.items()):
       d_final[k]=v+v2

  new_d=((sorted(d_final.items(),key= lambda x:x[1], reverse=True)))
 
  for i in range(m):
    print(new_d[i][0])
    
find_a([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],3)
