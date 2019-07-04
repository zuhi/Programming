#Given a range, print all numbers having unique digits.
def number_unique_digit(up,low):
  major=[]
  for i in range(up,low+1):
    num=i
    digit=[]
    while(num!=0):
      digit.append(num%10)
      num=num/10
    if(len(digit)==len(set(digit))):
      major.append(i)
  return(major)
print(number_unique_digit(10,20))
