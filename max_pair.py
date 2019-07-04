#Given an array with both +ive and -ive integers, return a pair with highest product.
def max_pair(a):
  pair=[]
  for i in a:
    for j in a:
      if(i!=j):
        pair.append([i,j])
  product=[]
  ind=[]
  for i in pair:
      ind.append(i)
      product.append(i[0]*i[1])
  print(ind[product.index(max(product))])
      
max_pair([1, 4, 3, 6, 7, 0])  
