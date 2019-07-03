#Check if a number can be expressed as x^y
import math
def check_(n):
  if(n==1):
    return(True)
  for x in range(2,int(math.sqrt(n)+1)):
        p=1
        while(p<n):
          pow_=pow(x,p)
          if(pow_==n):
                 return(True)
          p +=1
print(check_(8))
