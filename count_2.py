#Count words that appear exactly two times in an array of words

a=["hate", "love", "peace", "love", 
               "peace", "hate", "love", "peace", 
               "love", "peace"]
d=dict()
for i in a:
  if(i not in d):
    d[i]=1
  else:
    d[i]= d[i]+1
print(d)
rot=[]
for key,value in d.items():
  if(value==2):
    rot.append(key)
print(len(rot))
