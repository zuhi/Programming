#Print all possible strings that can be made by placing spaces
import itertools
str_="abcd"
n_space=[1]*(len(str_)-1)
n=(len(str_)-1)
table = list(itertools.product([0, 1], repeat=n))
list_=[]
for i in range(len(table)):
  st_=str_[0]
  for j in range(1,len(str_)):
    chck=j-1
    if(table[i][chck]==0):
      st_ += str_[j]
    else:
      st_ +=  " "+str_[j]
  list_.append(st_)
 print(list_)
