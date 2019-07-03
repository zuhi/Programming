#Given an array of distinct elements and a number x, find if there is a pair with a product equal to x
aray=[10, 20, 9, 40]
x= 400
def pair_exist(aray,x):
    product_=[]
    for i in range(len(aray)):
      for j in range(len(aray)):
        product_.append(aray[i]*aray[j])
    if( x in product_):
      return(True)
    else:
      return(False)
print(pair_exist(aray,x))
