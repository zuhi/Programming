#Given an interval, the task is to count numbers which have same first and last digits.
#For example, 1231 has same first and last digits
def same_1andlast(s,e):
  out=[]
  for i in range(s,e+1):
    num=i
    nos=[]
    while(num!=0):
      nos.append(num%10)
      num /= 10
    if(nos[0]==nos[len(nos)-1]):
      out.append(i)
  return(out,len(out))
print(same_1andlast(7,68))
