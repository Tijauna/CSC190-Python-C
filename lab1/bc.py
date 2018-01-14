def bc (stringInput):
  n = 0
  totalinputs = 0
  stringList = list(stringInput)
  stringLength = len(stringList)
  newstack = stack()
  
  for i in range(0,stringLength):
    if ((stringList[i] == '(') or (stringList[i] == '[') or (stringList[i] == '{')):
      n = n+1

      totalinputs = totalinputs+1
      
      newstack.push(stringList[i])
    
    elif ((stringList[i] == ')') or (stringList[i] == ']') or (stringList[i] == '}')):
      totalinputs = totalinputs+1
      print 'close'
      returnValue = newstack.pop()
      
      print returnValue
      
      
      if ((returnValue == '(') and (stringList[i] == ')')):
        failure = 0
        n = n -1
        
      elif ((returnValue == '[') and (stringList[i] == ']')):
        failure = 0
        n = n -1
        
      elif ((returnValue == '{') and (stringList[i] == '}')):
        failure = 0
        n = n -1
        
      else:
        failure = 1
        return [False,totalinputs-1]
        
  if ((failure == 0) and (n == 0)):
    return [True,'No Failure']
