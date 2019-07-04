#Given a string, find the first non-repeating character in it
#For example, if the input string is “GeeksforGeeks”, then output should be ‘f’ and if input string is “GeeksQuiz”, then output should be ‘G

st='GeeksforGeeks'
def func_(st):
  st_=set(st)
  for let_ in st_:
      count=0
      for i in st:
        if(let_ == i):
          count +=1
      if count == 1:
        return(let_)
  return(0)
print(func_(st))
