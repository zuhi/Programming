#Find and print the uncommon characters of the two given strings in sorted order.
#Here uncommon character means that either the character is present in one string or it is present in other string but not in both.
#The strings contain only lowercase characters and can contain duplicates
def uncommon_(s1,s2):
  s1=set(s1)
  s2=set(s2)
  unco=[]
  for s in s1:
    if(s not in s2):
      unco.append(s)
  for s in s2:
    if(s not in s1):
       unco.append(s)
  return(set(unco))
print(uncommon_("characters","alphabets"))
