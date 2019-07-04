#Given two strings in lowercase, the task is to make them anagram.
#The only allowed operation is to remove a character from any string.
#Find minimum number of characters to be deleted to make both the strings anagram?
def make_anagram(s1,s2):
  common=0
  for i in s1:
    if(i in s2):
      common += 1
  return(max(len(s1),len(s2))-common)
print(make_anagram("bcadeh","hea"))
