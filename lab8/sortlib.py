def selection_sort(u):
   
  for i in range (0,len(u)):
    minimum = i
   
    for j in range (i+1,len(u)):
      if u[minimum] > u[j]:
        minimum = j
    
    temp = u[i] 
    u[i] = u[minimum]
    u[minimum] = temp
     
  return True
  
  
#helper function for adding to heap 
def helper_store(heap,value,end):

  temp = 0
  done = 0
  
  heap[end] = value 
  
  if (end == 0):
    #print 'Adding to first position.'
    pass 
    
  else:
    
    while (done != 1):
        
      #for odd array position, must look up to right
      if (end%2 != 0):
        if heap[(end-1)/2] < heap[end]:
        
          #print "root upper right is smaller, swap"
          temp = heap[(end-1)/2]
          heap[(end-1)/2] = heap[end]
          heap[end] = temp
          end = (end-1)/2

        else:
          #print "upper right already bigger"
          done = 1
      
      
      #for even array position, must look up to left
      elif (end%2 == 0):
        if heap[(end-2)/2] < heap[end]:
          
          #print "root upper left is smaller"
          temp = heap[(end-2)/2]
          heap[(end-2)/2] = heap[end]
          heap[end] = temp
          end = (end-2)/2
        
        else:
          #print "upper left already bigger"
          done = 1

      if (end == 0):
        done = 1
  
  return 0;

#heap add function 
def heapify(u):
  heap = []
  for i in range (len(u)):
    heap = heap + [0]

  end = 0 
  
  #heap it
  for i in range (0,len(u)):
    helper_store(heap,u[i],i)
  
  
  
  for i in range (len(u)):
    u[i] = heap[i]

  
  return True 


#retrieve function 
def reheapify(u,end):
  
  temp = u[end]
  u[end] = u[0]
  u[0] = temp
  
  newList = [] 
  
  for i in range (0,end):
    newList = newList +[u[i]]

  heapify(newList)
  
  for i in range (0,end):
    u[i] = newList[i]

  return True 


def heap_sort(u):
  
  if len(u) == 0:
    return False 
    
  size = len(u)
  
  temp = 0
  rvalue = 0
  
  newSize = size

  heapify(u)
  
  for i in range (len(u)-1,-1,-1):
    currentend = i
    reheapify(u,currentend)
    
  return True 
  


def helper_merge_sort(u,left,mid,right):
  temp = [0]*len(u)
  
  left_end = mid - 1
  tmp_pos = left
  num_elements = right-left+1
  
  while (left <= left_end) and (mid <= right):
    if u[left] <= u[mid]:
      temp [tmp_pos] = u[left]
      tmp_pos = tmp_pos + 1
      left = left + 1
    else:
      temp [tmp_pos] = u[mid]
      tmp_pos = tmp_pos + 1
      mid = mid + 1 
      
  while (left <= left_end):
    temp [tmp_pos] = u [left]
    tmp_pos = tmp_pos + 1 
    left = left + 1 
  while (mid <= right):
    temp [tmp_pos] = u [mid]
    tmp_pos = tmp_pos + 1
    mid = mid + 1 
  
  for i in range (0,num_elements):
    u[right] = temp [right]
    right = right - 1
    
  
  
  return True
  
  
def helper_merge(u,left,right):
  if right > left:
    middlepoint = (left+right)/2
    helper_merge(u,left,middlepoint)
    helper_merge(u,middlepoint+1,right)
    helper_merge_sort(u,left,middlepoint+1,right)
    
  return True 
  
def merge_sort(u):
  if len(u) == 0:
    return False 
    
  helper_merge(u,0,len(u)-1)
  return True
  
  
   
