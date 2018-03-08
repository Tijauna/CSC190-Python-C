class queue:
    def __init__(self):
        self.storage=[]
        self.cnt = 0

    def empty(self):
       if self.cnt==0:
          return True
       else:
          return False

    def store(self,value):
        self.storage=self.storage+[value]
        self.cnt = self.cnt + 1
        return self.cnt

    def retrieve(self):
        if (self.cnt==0):
            return [False,0]
        else:
            r=self.storage[0]
            self.cnt=self.cnt-1
            self.storage=self.storage[1:]
            return [True,r]

class stack:
   def __init__(self):
      self.storage=[]
      self.count=0

   def empty(self):
      if (self.count==0):
         return True
      else:
         return False

   def store(self,x):
      self.storage = self.storage + [x]
      self.count = self.count + 1
      return True

   def retrieve(self):
      if (self.count==0):
         return [False,0]
      else:
         self.count = self.count - 1
         rval = self.storage[-1]
         self.storage = self.storage[0:-1]
         return [True,rval]


class graph:
  def __init__(self):
    self.store = []
    
  def addVertex(self,n):
    if n <= 0:
      return -1
    else:
      for i in range (0,n):
        length = len(self.store)
        self.store = self.store + [[[length]]]
      return len(self.store)
      
  def addEdge(self,from_idx,to_idx,directed,weight):
    if from_idx < 0 or to_idx < 0 or weight == 0:
      return False
    elif from_idx > len(self.store)-1 or to_idx > len(self.store)-1:
      return False
    else:
      if directed == True:
        self.store[from_idx] = self.store[from_idx] + [[to_idx,weight]]
      if directed == False:
        self.store[from_idx] = self.store[from_idx] + [[to_idx,weight]]
        self.store[to_idx] = self.store[to_idx] + [[from_idx,weight]]
      return True 
  
  def traverse(self,start,typeBreadth):
    
    totalOutput = list()
    
    if start != None and start < 0:
      print 'fail 0'
      return [] 
    
    elif start > len(self.store)-1:
      print 'fail too long'
      return []
      
    else:
      if typeBreadth == True:
        C = queue()
      elif typeBreadth == False:
        C = stack() 
      Discovered = []
      Processed = []
      output = []
      
      if start == None:
        
        
        for i in range (0, len(self.store)):
          
          Discovered = Discovered + [False]
          Processed = Processed + [False]
        

        
        for i in range (0, len(self.store)):
          output = list()
          if Discovered[i] == False:
             C.store(self.store[i])
             Discovered[i]=True
          
          while C.storage:

             w = C.retrieve()[1]
             #print w[0]
             
             if Processed[w[0][0]]==False:
                
                output = output + w[0]
                
                Processed[w[0][0]]=True

             for y in range (1, len(w)):
                x = w[y][0]
                #print x
                
                if Discovered[x] == False:
                    C.store(self.store[x])
                    Discovered[x]=True
          
          if(output):
            totalOutput = totalOutput + [output]      
      
      elif start != None:
        
        for i in range (0, len(self.store)):
          
          Discovered = Discovered + [False]
          Processed = Processed + [False]
    
        i = start
  
        if Discovered[i] == False:
           C.store(self.store[i])
           Discovered[i]=True
        
        while C.storage:
           w = C.retrieve()[1]
           #print w[0]
           
           if Processed[w[0][0]]==False:
              
              
              totalOutput = totalOutput + w[0]
              
              Processed[w[0][0]]=True

           for y in range (1, len(w)):
              x = w[y][0]
              #print x
              if Discovered[x] == False:
                  C.store(self.store[x])
                  Discovered[x]=True
                  
    
          
      return totalOutput
      
  def connectivity(self,vx,vy):
    output = [False,False]
    
    path = self.path(vx,vy)
    reversepath = self.path(vy,vx)
    if path[0]:
      output[0] = True
    if reversepath[0]:
      output[1] = True
    
    return output
    
    
  def path(self,vx,vy):
    output = self.traverse(vx,True)
    #print output
    
    for i in range (len(output)-1,-1,-1):
      if output[i] == vy:
        index = i
        break
      else:
        del output[i]
    
    for i in range(len(output)-2,0,-1):
      prevconnections = self.store[output[i]]
      connected = 0
      for j in range(len(prevconnections)-1,0,-1):
        if prevconnections[j][0] == output[i+1]:
          connected = 1
      if connected == 0:
        del output[i]

    output2 = self.traverse(vy,True)
    #print output2
    
    for i in range (len(output2)-1,-1,-1):
      if output2[i] == vx:
        index = i
        break
      else:
        del output2[i]
    
    for i in range(len(output2)-2,0,-1):
      prevconnections = self.store[output2[i]]
      connected = 0
      for j in range(len(prevconnections)-1,0,-1):
        if prevconnections[j][0] == output2[i+1]:
          connected = 1
      if connected == 0:
        del output2[i]
      
    finaloutput = [output,output2]

    return finaloutput


