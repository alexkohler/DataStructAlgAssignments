import sys
#visualizaiton - http://visualgo.net/bst.html
#All while loops within insert, transplant, and delete are iterating through the parents of the tree, and hence run in O(height(T)) which does not affect the runtime specifications
def insert(tree, z):
  #print "inserting " + str(z)
  parent = None
  new = Node(z)
  node = tree.root
  while node is not None:
    parent = node
    if new.data < node.data:
      #excuse the following finaggled wizardry
      if (node.minval - new.data < node.mingap and node.minval - new.data > 0):
         node.mingap = node.minval - new.data
      if node.minval < new.data:
        if (new.data - node.minval < node.mingap and new.data - node.minval >0):
          node.mingap = new.data - node.minval
        if (node.data - new.data < node.mingap):
          node.mingap = node.data - new.data     
      if node.minval > new.data:
        node.minval = new.data  
        if (node.minval - new.data < node.mingap and node.minval - new.data > 0):
            node.mingap = node.minval - new.data  
      elif (node.data - new.data < node.mingap and node.minval - new.data > 0):
        node.mingap = node.data - new.data
        node.minval = new.data
        if (node.data - new.data < node.mingap):
          node.mingap = node.data - new.data 
        if node.left is not None:
          if node.left.data - node.minval < node.mingap:
            node.mingap = node.left.data - node.minval

      #before updating node, ensure our minvals up the tree are correct
      if (node.parent is not None and node.mingap < node.parent.mingap):
        tmp = node
        while (tmp.parent is not None and tmp.mingap < tmp.parent.mingap): #iterating thru parents is O(height(T))
          tmp.parent.mingap = tmp.mingap
          tmp = tmp.parent      
      node = node.left
      #print "going left"
    else:
      if node.maxval < new.data:
        if (new.data - node.maxval < node.mingap):
          node.mingap = new.data - node.maxval
        node.maxval = new.data
      if (new.data - node.data < node.mingap):
          node.mingap = new.data - node.data
      #before updating node, ensure our minvals up the tree are correct
      if (node.parent is not None and node.mingap < node.parent.mingap):
        tmp = node
        while (tmp.parent is not None and tmp.mingap < tmp.parent.mingap): #iterating thru parents is O(height(T))
          tmp.parent.mingap = tmp.mingap
          tmp = tmp.parent          
      node = node.right
      #print "going right"

    if node is not None:  
      if parent.left is not None: 
          if parent.minval > z:
            parent.minval = z  
      else:
          parent.minval = parent.data    

  new.parent = parent
  if parent is None:
    tree.root = new
  elif new.data < parent.data:
    parent.left = new
    parent.left.minval = new.minval
  else:
    parent.right = new


    
  return new

#delete is called on a single node, so there should be no worries about calling your while loops on n nodes. (and moving your runtime up to nlogn)
def delete(tree, z):
  target = search(tree.root, z)
  if target is None:
    return None
  loveNode = None	
  if target.left is None:
    #print "d1"
    #if our right tree is also none, then min = max = itself
    transplant(tree, target, target.right)
    #pls refactor 2  
    if (tree.root.left is not None):    
      tree.root.minval = min(tree.root.data,tree.root.left.minval)
      tree.root.maxval = max(tree.root.data,tree.root.left.maxval)
      #mingap either in left or right subtree
      tree.root.mingap = min(tree.root.left.mingap, tree.root.data - tree.root.left.maxval)
      if (tree.root.right is not None):
        tree.root.minval = min(tree.root.minval, tree.root.right.minval)
        tree.root.maxval = max(tree.root.maxval, tree.root.right.maxval)
        #actual mingap at rt only checked here (because it was computed in left)
        tree.root.mingap = min(tree.root.right.mingap, tree.root.right.minval - tree.root.data, tree.root.mingap)
    elif (tree.root.right is not None):
      tree.root.minval = min(tree.root.data, tree.root.right.minval)
      tree.root.maxval = max(tree.root.data,tree.root.right.maxval)
      tree.root.mingap = min(tree.root.right.mingap, tree.root.right.minval - tree.root.data) 
    #pls refactor 2
    loveNode = target.parent #going out on a wing 
  elif target.right is None:
    #print "d2"
    loveNode = target.left
    transplant(tree, target, target.left)
    
  else:
    #print "d3"
    node = minimum(target.right)
    if node.parent is not target:
      transplant(tree, node, node.right)
      node.right = target.right
      node.right.parent = node    
    transplant(tree, target, node)
    node.left = target.left
    node.left.parent = node
    #pls refactor 2
    if (tree.root.left is not None):
      tree.root.minval = min(tree.root.data,tree.root.left.minval)
      tree.root.maxval = max(tree.root.data,tree.root.left.maxval)
      tree.root.mingap = min(tree.root.left.mingap, tree.root.data - tree.root.left.maxval)
      if (tree.root.right is not None):
        tree.root.minval = min(tree.root.minval, tree.root.right.minval)
        tree.root.maxval = max(tree.root.maxval, tree.root.right.maxval)
        #actual mingap at rt only checked here (because it was computed in left)
        tree.root.mingap = min(tree.root.mingap, tree.root.right.mingap, tree.root.right.minval - tree.root.data)
    elif (tree.root.right is not None):
      tree.root.minval = min(tree.root.data, tree.root.right.minval)
      tree.root.maxval = max(tree.root.data,tree.root.right.maxval)
      tree.root.mingap = min(tree.root.right.minval - tree.root.data, tree.root.right.mingap)
    #pls refactor 2
    loveNode = node
      
  v = loveNode
  if v is not None:
    if (v.left is not None):
      v.minval = min(v.data,v.left.minval)
      v.maxval = max(v.data,v.left.maxval)
      v.mingap = min(v.left.mingap, v.data - v.left.maxval)
      if (v.right is not None):
        v.minval = min(v.minval, v.right.minval)
        v.maxval = max(v.maxval, v.right.maxval)
        v.mingap = min(v.mingap, v.right.mingap, v.right.minval - v.data)
    elif (v.right is not None):
      v.minval = min(v.data, v.right.minval)
      v.maxval = max(v.data,v.right.maxval)
      v.mingap = min(v.right.mingap, v.right.minval - v.data)
        
            
            
    #carry up if necessary (FINAL STEP)
    treeIter = v.parent
    while (treeIter is not None): #iterating thru parents is O(height(T))
      if (treeIter.left is not None):
        treeIter.mingap = min(treeIter.left.mingap, treeIter.data - treeIter.left.maxval)
        treeIter.minval = min(treeIter.left.minval, treeIter.data)
        if (treeIter.right is not None):
          #only check mingap here (embedded if)
          treeIter.maxval = max(treeIter.data, treeIter.right.maxval)
          treeIter.mingap = min(treeIter.mingap, treeIter.right.mingap, treeIter.right.minval - treeIter.data)
      elif (treeIter.right is not None):
        treeIter.maxval = max(treeIter.data, treeIter.right.maxval)
        treeIter.mingap = min(treeIter.right.minval - treeIter.data, treeIter.right.mingap)
      treeIter = treeIter.parent  
      


  return target


def transplant(tree, u, v):
  if u.parent is None: #smallest element (succesor) in right subtree moves up
    #print "t1"
    v.minval = tree.root.minval
    tree.root = v
  elif u is u.parent.left:
    #print "t2"
    u.parent.left = v

    #pls refactor
    if u.parent.left is None and u.parent.right is None:#we now have a leaf
      u.parent.minval = u.parent.data
      u.parent.maxval = u.parent.data
      u.parent.mingap = sys.maxsize
    if u.parent.parent is not None and u.parent.left is not None:
        treeIter = u.parent.parent
        while (treeIter is not None): ##iterating thru parents is O(height(T)) 
          if (u.parent.minval < treeIter.data):
            treeIter.minval = min(u.parent.data, u.parent.left.minval)
          if (u.parent.maxval > treeIter.data):
            treeIter.maxval = u.parent.data
          treeIter = treeIter.parent
        
    elif (u.parent.parent is not None and u.parent.parent.left is not None):
      treeIter = u.parent.parent
      while (treeIter is not None and treeIter.left is not None):#iterating thru parents is O(height(T))
        if treeIter.left.minval is not u.data:
          treeIter.minval = min(treeIter.data, treeIter.left.minval)
        else:
          treeIter.minval = min(treeIter.data, treeIter.left.data)
        treeIter = treeIter.parent 
        
     #pls refactor     
  else:
    #print "t3"
    u.parent.right = v
    if (u.parent.left is not None):
      u.parent.mingap = min(u.parent.left.mingap, u.parent.data - u.parent.left.maxval)
      
      treeIter = u.parent
      while (treeIter is not None and treeIter.left is not None and treeIter.left.minval < treeIter.minval): #iterating thru parents is O(height(T))
        treeIter.minval = treeIter.left.minval
        treeIter = treeIter.parent
        
    if (u.parent.right is None):
      u.parent.maxval = u.parent.data

    if u.parent.left is None and u.parent.right is None:#u.parent is a leaf

      u.parent.minval = u.parent.data
      u.parent.maxval = u.parent.data
      u.parent.mingap = sys.maxsize
      
      if u.parent.parent is not None:     
        treeIter = u.parent.parent
        while (treeIter is not None and u.parent.minval < treeIter.data): #iterating thru parents is O(height(T)) 
          if (u.parent.minval < treeIter.data):
            treeIter.minval = u.parent.data
          if (u.parent.maxval > treeIter.data):
            treeIter.maxval = u.parent.data
          treeIter = treeIter.parent
  
    #pls refactor
  if v is not None:
    #print "t4"
    v.parent = u.parent
    if v.parent is not None and v.parent.left is not None:
    	v.parent.mingap = min(v.parent.left.mingap, v.parent.data - v.parent.left.maxval)
  #fix root      
  if (tree.root.left is not None):
    tree.root.minval = min(tree.root.data,tree.root.left.minval)
    tree.root.maxval = max(tree.root.data,tree.root.left.maxval)
    tree.root.mingap = min(tree.root.left.mingap, tree.root.data - tree.root.left.maxval)
    if (tree.root.right is not None):
      tree.root.minval = min(tree.root.minval, tree.root.right.minval)
      tree.root.maxval = max(tree.root.maxval, tree.root.right.maxval)
      tree.root.mingap = min(tree.root.mingap, tree.root.right.minval - tree.root.data)
  elif (tree.root.right is not None):
    tree.root.minval = min(tree.root.data, tree.root.right.minval)
    tree.root.maxval = max(tree.root.data,tree.root.right.maxval)
    tree.root.mingap = tree.root.right.minval - tree.root.data

def minimum(node):
  #
  #MODIFY IN THE CODE IF NEEDED....
  # 
  if node is not None:
    while node.left is not None:
      node = node.left    
  return node

def printMin(root):
  if root is None:
    return;
  print str(root.data) + " minval: " + str(root.minval) + "| maxval: " + str(root.maxval) + "| mingap " + str(root.mingap)
  printMin(root.left)
  printMin(root.right)
  
#  
#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE, BUT YOU CAN IF YOU WANT
#



def search(node, z):
  #
  #YOU DO NOT NEED TO MODIFY THIS FUNCTION....
  # 
  while node is not None:
    if z == node.data:
      return node
    elif z < node.data:
      node = node.left
    else:
      node = node.right
  return None


#tree class
#YOU DO NOT NEED TO CHANGE THIS CLASS
class BST(object):
  def __init__(self):
    self.root = None

#node class
class Node(object):
  def __init__(self, val):
    self.left = None
    self.right = None
    self.parent = None
    self.data = val
    self.mingap = sys.maxsize #YOU WANT TO MAKE SURE THAT THIS ATTRIBUE IS ALWAYS MAINTAINED CORRECTLY
    self.minval = val #YOU WANT TO MAKE SURE THAT THIS ATTRIBUE IS ALWAYS MAINTAINED CORRECTLY
    self.maxval = val #YOU WANT TO MAKE SURE THAT THIS ATTRIBUE IS ALWAYS MAINTAINED CORRECTLY
    

#This function takes care of building the tree according to specifications and outputing the min-gap after each operation as required.
def ads_test(data):

  n = len (data)
  tree = BST()  #create an empty BST
  winserted = None
  for i in range(0,n):
    #perform required operation on the BST 
    if data[i][0] == 'I':
      insert(tree, int(data[i][1:]))
      winserted = "I" + str(data[i][1:])
    elif data[i][0] == 'D':
      delete(tree, int(data[i][1:]))
      winserted = "D" + str(data[i][1:])
      
    #if i == n -1:
      #printMin(tree.root)
    #if this is not the first element, then output the value of the min gap after this operation
    #if i > 0:
      #print str(tree.root.mingap) + " (" + str(winserted) + "),",
    if i > 0:
      print tree.root.mingap,



#Read input
f = open("input.txt", "r")
data = f.readline().split()

#Fill in the augmented data structure with the input and generate the appropriate output
ads_test(data)      
