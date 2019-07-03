#Check if a given Binary Tree is SumTree
class Node:
  
  def __init__(self,key):
    self.key= key
    self.left= None
    self.right= None
def sum_(a,b):
  return(a+b)
    
def get_sum(root):

  if(root is None):
    return
  else:
    if(root.right!=None and root.left!=None):
       if(sum_(root.right.key,root.left.key)==root.key):
          return(True)
          
    elif(root.right!=None or root.left!=None):
      if(root.right!=None):
        get_sum(root.right)
      else:
        get_sum(root.left)
    else:
      return(False)
      
      
root = Node(2) 
root.left = Node(1) 
root.right = Node(1)
root.left.left=Node(3)
print(get_sum(root))
