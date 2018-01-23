# coding: utf-8
import tree 

class queue:
  def __init__(self):
    self.store = []
    self.length = 0
          
  def push(self, value):
    self.store = self.store + [value]
    self.length = self.length + 1
    
  def pop(self):
    if self.length == 0:
      return False
    returnValue = self.store[0]
    del self.store[0]
    self.length = self.length - 1
    #print "***Popped: ",returnValue
    return returnValue

class binary_tree:
    def __init__(self,x):
        self.store = [x,[],[]]

    def AddLeft(self,x):
        self.store[1] = self.store[1] + [x]
        return True
        
    def AddRight(self,x):
        self.store[2] = self.store[2] + [x]
        return True
        
    def Helper(self, indentlevel):
        print self.store[0]
        
        #length = length of the list in the fake binary tree
        for i in range (len(self.store[1])):
        
          temp = self.store[1][i]
          
          #tab character
          for j in range (0, indentlevel):
            print "\t",
      
          temp.Helper(indentlevel+1)
          
          
        for i in range (len(self.store[2])):
        
          temp = self.store[2][i]
          
          #tab character
          for j in range (0, indentlevel):
            print "\t",
      
          temp.Helper(indentlevel+1)

          
    def Print_DepthFirst(self):
      
        self.Helper(1)
        return 0
        
    def Get_LevelOrder (self):
      Q1 = queue()
      
      #push on, then push on the children, then popList
      #push the entire list in first
      Q1.push(self)
      
      popList = []
      
      #check for children
      Failure = 0
      
      while (Failure != 1):
        try:
          popped = Q1.pop()
          popList = popList + [popped.store[0]]
        except:
          Failure = 1
          break
        
        #push in the children lists
        if (popped.store[1] != None):
    
          #push in the children lists
          for i in range (len(popped.store[1])):
            Q1.push(popped.store[1][i])
        
        if (popped.store[2] != None):
    
          #push in the children lists
          for i in range (len(popped.store[2])):
            Q1.push(popped.store[2][i])
        
      return popList   
      
    #print convertedbinary.store[0] #1000
    #print convertedbinary.store[1][0].store[0] #2000
    #print convertedbinary.store[1][0].store[1][0].store[0] #6
    #print convertedbinary.store[1][0].store[2][0].store[0] #3000
    #print convertedbinary.store[1][0].store[1][0].store[1][0].store[0] #8
    #print convertedbinary.store[1][0].store[1][0].store[2][0].store[0] #7
    #print convertedbinary.store[1][0].store[2][0].store[1][0].store[0] #5
    #print convertedbinary.store[1][0].store[1][0].store[2][0].store[2][0].store[0] #2

    def ConvertToTreeHelper (self):
      
      #print self.store[0]
      newTree = tree.tree(self.store[0])
      
      #are there left successors?
      try:
        if (self.store[1][0]!= None):
          
          newTree2 = self.store[1][0]
          #print "First Successor",newTree2.store[0],""
          #print "Added to",newTree.store[0],""
          
  
          newTree.AddSuccessor(newTree2.ConvertToTreeHelper())
          
          if newTree2.store[2]!= None:
            
            newTree3 = newTree2.store[2][0]
            
            while (newTree3):
              newTree.AddSuccessor(newTree3.ConvertToTreeHelper())
              newTree3 = newTree3.store[2][0]

      except:
        print 'No More Successors'
      
      return newTree
      
    def ConvertToTree(self):
      returnList = [False, []]
      
      if self.store[2]:
        print 'Error, root has right subtree. Cannot convert to binary.'
        returnList[0] = False
        
      else:
        returnList[1] = self.ConvertToTreeHelper()
        returnList[0] = True
        
      return returnList
          
        
