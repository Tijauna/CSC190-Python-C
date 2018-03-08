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
