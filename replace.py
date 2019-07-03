#Replace all ‘0’ with ‘5’ in an input Integer
def get_number(no):
  old=0
  count=0
  while(no!=0):
    numb=no%10
    no /=10
    if(numb==0):
      numb=5
    old += numb * pow(10,count)
    count += 1
  print(old)
get_number(10120)
