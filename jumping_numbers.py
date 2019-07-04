#A number is called as a Jumping Number if all adjacent digits in it differ by 1. 
#The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping Numbers.
#For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.
#Given a positive number x, print all Jumping Numbers smaller than or equal to x. The numbers can be printed in any order.

def count_(no):
  ar=list()
  if( no<11):
    for i in range(no):
      ar.append(i)
  else:
    for i in range(11):
      ar.append(i)
    for j in range(11,no+1):
      num=j
      n=j
      count=0
      diff=[]
      while(num!=0):
        last=num%10
        num=num/10

        if(count>=1):
             diff.append(last-prev)
        prev=last
        count += 1
      check_var=0
      for i in diff:
        if(i==1 or i==-1):
          check_var += 1
      if(check_var==(count-1)):
        ar.append(n)
    return(ar)
  
print(count_(105))
