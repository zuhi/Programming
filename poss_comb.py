#Given a number d, representing the number of digits of a positive integer.
#Find the total count of positive integer (consisting of d digits exactly) which have at-least one zero in them
def possible_nos(d):
  return(9*(pow(10,d-1)-pow(9,d-1)))
print(possible_nos(1))
