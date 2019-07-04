#Given a dictionary of words,
#ind all strings that matches the given pattern where every character in the pattern is uniquely mapped to a character in the dictionary
a=["abb", "abc", "xyz", "xyy"]
def check_(a,pattern):
  major=[]
  d_pat=dict()
  for i in pattern:
    if(i not in d_pat):
      d_pat[i]=1
    else:
      d_pat[i] += 1
  for i in a:
    d_to = dict()
    for j in i:
      if(j not in d_to):
        d_to[j]=1
      else:
        d_to[j] +=1
    if(len(d_pat)==len(d_to)):
      c=0
      for k,m in zip(i,pattern):
        if(d_to[k]==d_pat[m]):
          c += 1

      if(c==len(pattern)):
        major.append(i)
  return(major)
print(check_(a,"foo"))
