# coding: utf-8
import binary_tree

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


class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True
        
#print x.store[0] 1000
#print x.store[1][0].store[0] 2000
#print x.store[1][0].store[1][0].store[0] 6
#print x.store[1][0].store[1][1].store[0] 7
#print x.store[1][1].store[0] 3000
#print x.store[1][1].store[1][0].store[0] 5
       
    def Helper(self, indentlevel):
        print self.store[0]
        
        #length = length of the list in the fake binary tree
        for i in range (len(self.store[1])):
          temp = self.store[1][i]
          
          #tab character
          for j in range (0, indentlevel):
            print "\t",
      
          temp.Helper(indentlevel+1)
        return 0
          
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
          
        if (popped.store[1] != None):
    
          #push in the children lists
          for i in range (len(popped.store[1])):
            Q1.push(popped.store[1][i])
            
      return popList

    def LevelHelper(self, Q1):
   
      #check for children 
      if (self.store[1] != None):
        
        self.LevelPusher(Q1)

        for i in range (len(self.store[1])):
          temp2 = self.store[1][i]
          print "   Finding children of:", temp2.store[0],""
          temp2.LevelHelper(Q1)
    
    def LevelPusher(self, Q1):
      #push on children of current value 
        for i in range (len(self.store[1])):

          Q1.push(self.store[1][i].store[0])
          print "Pushing: ",self.store[1][i].store[0],""
    
    def Get_LevelOrderOld (self):
      Q1 = queue()
      Q1.push(self.store[0])

      self.LevelHelper(Q1)
      popList = []
      for i in range (Q1.length):
        popList = popList + [Q1.pop()]
        
      return popList
      
    def ConvertToBinaryTree (self):
    
      newBinary = binary_tree.binary_tree(self.store[0])
      
      
      #are there successors?
      if (self.store[1]!= None):
        
        for i in range (0,len(self.store[1])):
        
          
          #check for first successor
          if (i == 0):
            newBinary2 = self.store[1][i].ConvertToBinaryTree()
            #print "Left",newBinary2.store[0],""
            #print "Added to",newBinary.store[0],""
            newBinary.AddLeft(newBinary2)
          
          #subsequent successors
          else:
            newBinary3 = self.store[1][i].ConvertToBinaryTree()
            #print "Right",newBinary3.store[0],""
            #print "Added to",newBinary2.store[0],""
            newBinary2.AddRight(newBinary3)
            newBinary2 = newBinary3
            
      return newBinary
      
