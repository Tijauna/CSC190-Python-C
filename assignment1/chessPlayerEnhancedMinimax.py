#white: Offset=10
#Black: Offset=20

#Piece: Value
#Pawn:   +0
#Knight: +1
#Bishop: +2
#Rook:   +3
#Queen:  +4
#King:   +5

import random 

def GetPlayerPositions(board,player):
  output = []
  
  #white = 10, black = 20
  if (player == 10):
    for i in range (0,64):
      if ((board[i] != 0) and (board[i] < 20) and (board[i] >= 10)):
        output = output + [i]
      
  elif (player == 20):
    for i in range (0,64):
      if ((board[i] != 0) and (board[i] >= 20)):
        output = output + [i]    
  
  return output
  
def rowchecker (position):
  row1 = []
  row2 = []
  row3 = []
  row4 = []
  row5 = []
  row6 = []
  row7 = []
  row8 = []
  
  for i in range (0,8):
    row1 = row1 + [i]
    row2 = row2 + [i+8]
    row3 = row3 + [i+16]
    row4 = row4 + [i+24]
    row5 = row5 + [i+32]
    row6 = row6 + [i+40]
    row7 = row7 + [i+48]
    row8 = row8 + [i+56]
  
  row = 0
  
  for i in range (0,8):
    if position == row1[i]:
      row = 1
    elif position == row2[i]:
      row = 2
    elif position == row3[i]:
      row = 3
    elif position == row4[i]:
      row = 4
    elif position == row5[i]:
      row = 5
    elif position == row6[i]:
      row = 6
    elif position == row7[i]:
      row = 7
    elif position == row8[i]:
      row = 8
    
  return row 





def GetPieceLegalMoves(board,position):
  output = []
  
  #white = 10, black = 20  
  # +8 for going one row up
  # -8 for going one row down 
  
  #no piece at position
  if (board[position] == 0):
    print 'No piece at this position.'
    return output
  
  #pawn white
  if (board[position] == 10):
    leftedge = 0
    rightedge = 0
    
    #check for left edge
    for i in range (0,64,8):
      if (position == i):
        #print 'Pawn is on left edge.'
        leftedge = 1
        
        
    #check for right edge
    for i in range (7,71,8):
      if (position == i):
        #print 'Pawn is on right edge.'
        rightedge = 1
        
    #check for opposite end of board
    for i in range (56,64):
      if (position == i):
        #print 'Pawn is at end of board. No moves possible.'
        return output
    
    #one step forward move, cannot capture forward 
    if (board[position+8] == 0):
      output = output + [position+8]
    
    #left forward move and capture
    if (leftedge != 1):
      if (board[position+7] >= 20):
        output = output + [position+7]
    
    #right forward move and capture 
    if (rightedge != 1):
      if (board[position+9] >= 20):
        output = output + [position+9]
    
    
    return output
        
  #pawn black
  if (board[position] == 20):
    leftedge = 0
    rightedge = 0
    
    #check for right edge
    for i in range (63,-1,-8):
      if (position == i):
        #print 'Pawn is on right edge.'
        rightedge = 1
        
        
    #check for left edge
    for i in range (63,-1,-8):
      if (position == i):
        #print 'Pawn is on left edge.'
        leftedge = 1
        
    #check for opposite end of board
    for i in range (0,8):
      if (position == i):
        #print 'Pawn is at end of board. No moves possible.'
        return output
    
    #one step forward move, cannot capture forward 
    if (board[position-8] == 0):
      output = output + [position-8]
    
    #left forward move and capture
    if (leftedge != 1):
      if ((board[position-7] < 20) and (board[position-7] > 0)):
        output = output + [position-7]
    
    #right forward move and capture 
    if (rightedge != 1):
      if ((board[position-9] < 20) and (board[position-9] > 0)):
        output = output + [position-9]
    
    return output    
      
  #white knight
  if (board[position] == 11):
    
    initialrow = rowchecker(position)
      
    try:
      if ((board[position+6] == 0) or (board[position+6] >= 20)):
        if rowchecker(position+6) == initialrow+1:
          output = output + [position+6]
    except:
      #print 'Knight move not possible'
      pass
    
    try:
      if ((board[position+15] == 0) or (board[position+15] >= 20)):
        if rowchecker(position+15) == initialrow+2:
          output = output + [position+15]
    except:
      #print 'Knight move not possible'
      pass
    
    try:
      if ((board[position+17] == 0) or (board[position+17] >= 20)):
        if rowchecker(position+17) == initialrow+2:
          output = output + [position+17]
    except:
      #print 'Knight move not possible'
      pass
    
    try:
      if ((board[position+10] == 0) or (board[position+10] >= 20)):
        if rowchecker(position+10) == initialrow+1:
          output = output + [position+10]
    except:
      #print 'Knight move not possible'
      pass
      
    try:
      if position-10 >= 0:
        if ((board[position-10] == 0) or (board[position-10] >= 20)):
          if rowchecker(position-10) == initialrow-1:
            output = output + [position-10]
    except:
      #print 'Knight move not possible'
      pass
      
    try:
      if position-17 >= 0:
        if ((board[position-17] == 0) or (board[position-17] >= 20)):
          if rowchecker(position-17) == initialrow-2:
            output = output + [position-17]
    except:
      #print 'Knight move not possible'
      pass
      
    try:
      if position-15 >= 0:
        if ((board[position-15] == 0) or (board[position-15] >= 20)):
          if rowchecker(position-15) == initialrow-2:
            output = output + [position-15]
    except:
      #print 'Knight move not possible'
      pass
      
    try:
      if position-6 >= 0:
        if ((board[position-6] == 0) or (board[position-6] >= 20)):
          if rowchecker(position-6) == initialrow-1:
            output = output + [position-6]
    except:
      #print 'Knight move not possible'
      pass

    return output
    
  #black knight
  if (board[position] == 21):
    
    
    initialrow = rowchecker(position)
      
    try:
      if ((board[position+6] == 0) or (board[position+6] <20)):
        if rowchecker(position+6) == initialrow+1:
          output = output + [position+6]
    except:
      #print 'Knight move not possible'
      pass
    
    try:
      if ((board[position+15] == 0) or (board[position+15] <20)):
        if rowchecker(position+15) == initialrow+2:
          output = output + [position+15]
    except:
      #print 'Knight move not possible'
      pass
    
    try:
      if ((board[position+17] == 0) or (board[position+17] <20)):
        if rowchecker(position+17) == initialrow+2:
          output = output + [position+17]
    except:
      #print 'Knight move not possible'
      pass

    try:
      if ((board[position+10] == 0) or (board[position+10] <20)):
        if rowchecker(position+10) == initialrow+1:
          output = output + [position+10]
    except:
      #print 'Knight move not possible'
      pass
      
    try:
      if position-10 >= 0:
        if ((board[position-10] == 0) or (board[position-10] <20)):
          if rowchecker(position-10) == initialrow-1:
            output = output + [position-10]
    except:
      #print 'Knight move not possible'
      pass
      
    try:
      if position-17 >= 0:
        if ((board[position-17] == 0) or (board[position-17] <20)):
          if rowchecker(position-17) == initialrow-2:
            output = output + [position-17]
    except:
      #print 'Knight move not possible'
      pass
      
    try:
      if position-15 >= 0:
        if ((board[position-15] == 0) or (board[position-15] <20)):
          if rowchecker(position-15) == initialrow-2:
            output = output + [position-15]
    except:
      #print 'Knight move not possible'
      pass
      
    try:
      if position-6 >= 0:
        if ((board[position-6] == 0) or (board[position-6] <20)):
          if rowchecker(position-6) == initialrow-1:
            output = output + [position-6]
    except:
      #print 'Knight move not possible'
      pass

    return output
  
  #white bishop
  if (board[position] == 12):   
    failure = 0
    additional = 7
    
    if position == 56:
      for i in range (49,0,-7):
        if board[i] == 0:
          output = output + [i]
        elif board[i] >= 20:
          output = output + [i]
          break
        elif board[i] <= 20 and board[i] >= 10:
          break
        
    elif position == 63:
      for i in range (54,-9,-9):
        if board[i] == 0:
          output = output + [i]
        elif board[i] >= 20:
          output = output + [i]
          break
        elif board[i] <= 20 and board[i] >= 10:
          break
        
    else:
      while (failure==0):
        if position+additional >= 0:
          try:
            #check for left edge
            for i in range (0,64,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
            
            if (failure != 1):
              #check for opposite end of board
              for i in range (56,64):
                if (position+additional == i):
                  failure = 1
                  if (board[position+additional] == 0):
                    output = output + [position+additional]
                    failure = 1
                  elif (board[position+additional] >= 20):
                    output = output + [position+additional]
                    failure = 1
                    
                elif position == i:
                  failure = 1
            
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] < 20):
                failure = 1
                
          except:
            failure = 1
        else:
          failure = 1
        additional = additional+7
        
      failure = 0
      additional = 9
      
      while (failure==0):
        if position+additional >= 0:
          try:
            #check for right edge
            for i in range (7,71,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
            
            if (failure != 1):
              #check for opposite end of board
              for i in range (56,64):
                if (position+additional == i):
                  failure = 1
                  if (board[position+additional] == 0):
                    output = output + [position+additional]
                    failure = 1
                  elif (board[position+additional] >= 20):
                    output = output + [position+additional]
                    failure = 1
                    
                elif position == i:
                  failure = 1
            
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] < 20):
                failure = 1
                
          except:
            failure = 1
        else:
          failure = 1
        additional = additional+9
        
      failure = 0
      additional = -9
      
      while (failure==0):
        if position+additional >= 0:
          try:
            #check for left edge
            for i in range (0,64,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
            
            if (failure != 1):
              #check for opposite end of board
              for i in range (0,8):
                if (position+additional == i):
                  failure = 1
                  if (board[position+additional] == 0):
                    output = output + [position+additional]
                    failure = 1
                  elif (board[position+additional] >= 20):
                    output = output + [position+additional]
                    failure = 1
                    
                elif position == i:
                  failure = 1
            
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] < 20):
                failure = 1
                
          except:
            failure = 1
        else:
          failure = 1
        additional = additional-9
      
      failure = 0
      additional = -7
      
      while (failure==0):
        if position+additional >= 0:
          try:
            #check for right edge
            for i in range (7,71,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
            
            if (failure != 1):
              #check for opposite end of board
              for i in range (0,8):
                if (position+additional == i):
                  failure = 1
                  if (board[position+additional] == 0):
                    output = output + [position+additional]
                    failure = 1
                  elif (board[position+additional] >= 20):
                    output = output + [position+additional]
                    failure = 1
                    
                elif position == i:
                  failure = 1
            
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] < 20):
                failure = 1
                
          except:
            failure = 1
        else:
          failure = 1
        additional = additional-7
      
    return output 
    
  #black bishop
  if (board[position] == 22):   
    failure = 0
    additional = 7
    
    if position == 56:
      for i in range (49,0,-7):
        if board[i] == 0:
          output = output + [i]
        elif board[i] >= 20:
          break
        elif board[i] <= 20 and board[i] >= 10:
          output = output + [i]
          break
        
    elif position == 63:
      for i in range (54,-9,-9):
        if board[i] == 0:
          output = output + [i]
        elif board[i] >= 20:
          break
        elif board[i] <= 20 and board[i] >= 10:
          output = output + [i]
          break
        
    else:
    
      while (failure==0):
        if position+additional >= 0:
          try:
            #check for left edge
            for i in range (0,64,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
            
            if (failure != 1):
              #check for opposite end of board
              for i in range (56,64):
                if (position+additional == i):
                  failure = 1
                  if (board[position+additional] == 0):
                    output = output + [position+additional]
                    failure = 1
                  elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                    output = output + [position+additional]
                    failure = 1
                
                elif position == i:
                  failure = 1
            
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                failure = 1
                
          except:
            failure = 1
        else:
          failure = 1
        additional = additional+7
        
      failure = 0
      additional = 9
      
      while (failure==0):
        if position+additional >= 0:
          try:
            #check for right edge
            for i in range (7,71,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
            
            if (failure != 1):
              #check for opposite end of board
              for i in range (56,64):
                if (position+additional == i):
                  failure = 1
                  if (board[position+additional] == 0):
                    output = output + [position+additional]
                    failure = 1
                  elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                    output = output + [position+additional]
                    failure = 1
                    
                elif position == i:
                  failure = 1
            
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                failure = 1
                
          except:
            failure = 1
        else:
          failure = 1
        additional = additional+9
        
      failure = 0
      additional = -9
      
      while (failure==0):
        if position+additional >= 0:
          try:
            #check for left edge
            for i in range (0,64,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
            
            if (failure != 1):
              #check for opposite end of board
              for i in range (0,8):
                if (position+additional == i):
                  failure = 1
                  if (board[position+additional] == 0):
                    output = output + [position+additional]
                    failure = 1
                  elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                    output = output + [position+additional]
                    failure = 1
                    
                elif position == i:
                  failure = 1
            
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                failure = 1
                
          except:
            failure = 1
        else:
          failure = 1
        additional = additional-9
      
      failure = 0
      additional = -7
      
      while (failure==0):
        if position+additional >= 0:
          try:
            #check for right edge
            for i in range (7,71,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
            
            if (failure != 1):
              #check for opposite end of board
              for i in range (0,8):
                if (position+additional == i):
                  failure = 1
                  if (board[position+additional] == 0):
                    output = output + [position+additional]
                    failure = 1
                  elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                    output = output + [position+additional]
                    failure = 1
                    
                elif position == i:
                  failure = 1
            
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                failure = 1
                
          except:
            failure = 1
        else:
          failure = 1
        additional = additional-7
    
    return output    
    
    
  #white rook
  if (board[position] == 13):   
    failure = 0
    additional = 8
    
    while (failure==0):
      try:
        
          #check for top of board
          for i in range (56,64):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0)and (position+additional >= 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20)and (position+additional >= 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
            
      except:
        failure = 1
      additional = additional+8
      
    failure = 0
    additional = -8
    
    while (failure==0):
      try:
        
          #check for bottom of board
          for i in range (0,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
            
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0)and (position+additional >= 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20)and (position+additional >= 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
            
      except:
        failure = 1
      additional = additional-8
      
    failure = 0
    additional = -1
    
    while (failure==0):
      try:
        
          #check for left of board
          for i in range (0,64,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0)and (position+additional >= 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20)and (position+additional >= 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
            
      except:
        failure = 1
      additional = additional-1
      
    failure = 0
    additional = 1
    
    while (failure==0):
      try:
        
          #check for right of board
          for i in range (7,71,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
            
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0)and (position+additional >= 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20) and (position+additional >= 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
            
      except:
        failure = 1
      additional = additional+1
    
    return output    
  
    #black rook
  if (board[position] == 23):   
    failure = 0
    additional = 8
    
    while (failure==0):
      try:
        
          #check for top of board
          for i in range (56,64):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0) and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)) and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0) and (position+additional >= 0):
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10)) and (position+additional >= 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
            
      except:
        failure = 1
      additional = additional+8
      
    failure = 0
    additional = -8
    
    while (failure==0):
      try:
        
          #check for bottom of board
          for i in range (0,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0)and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional >= 0)):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0) and (position+additional >= 0):
              output = output + [position+additional]
            elif (board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional >= 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
            
      except:
        failure = 1
      additional = additional-8
      
    failure = 0
    additional = -1
    
    while (failure==0):
      try:
        
          #check for left of board
          for i in range (0,64,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0) and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional >= 0)):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0) and (position+additional >= 0):
              output = output + [position+additional]
            elif (board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional >= 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
            
      except:
        failure = 1
      additional = additional-1
      
    failure = 0
    additional = 1
    
    while (failure==0):
      try:
        
          #check for right of board
          for i in range (7,71,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0) and (position+additional >= 0):
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional >= 0)):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0) and (position+additional >= 0):
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional >= 0)):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
            
      except:
        failure = 1
      additional = additional+1
    
    return output 
    
  
  #white queen
  if (board[position] == 14):   
    failure = 0
    additional = 7
    
    while (failure==0):
      if position+additional >= 0:
        try:
          #check for left edge
          for i in range (0,64,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
          
          if (failure != 1):
            #check for opposite end of board
            for i in range (56,64):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional+7
      
    failure = 0
    additional = 9
    
    while (failure==0):
      if position+additional >= 0:
        try:
          #check for right edge
          for i in range (7,71,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
          
          if (failure != 1):
            #check for opposite end of board
            for i in range (56,64):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional+9
      
    failure = 0
    additional = -9
    
    while (failure==0):
      if position+additional >= 0:
        try:
          #check for left edge
          for i in range (0,64,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
          
          if (failure != 1):
            #check for opposite end of board
            for i in range (0,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional-9
    
    failure = 0
    additional = -7
    
    while (failure==0):
      if position+additional >= 0:
        try:
          #check for right edge
          for i in range (7,71,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
          
          if (failure != 1):
            #check for opposite end of board
            for i in range (0,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional-7

    failure = 0
    additional = 8
    
    while (failure==0):
      if position+additional >= 0:
        try:
          
            #check for top of board
            for i in range (56,64):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] < 20):
                failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional+8
      
    failure = 0
    additional = -8
    
    while (failure==0):
      if position+additional >= 0:
        try:
          
            #check for bottom of board
            for i in range (0,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] < 20):
                failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional-8
      
    failure = 0
    additional = -1
    
    while (failure==0):
      if position+additional >= 0:
        try:
          
            #check for left of board
            for i in range (0,64,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] < 20):
                failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional-1
      
    failure = 0
    additional = 1
    
    while (failure==0):
      if position+additional >= 0:
        try:
          
            #check for right of board
            for i in range (7,71,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif (board[position+additional] >= 20):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] < 20):
                failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional+1
    
    return output 
 
   
  
  #black queen
  if (board[position] == 24):
    failure = 0
    additional = 7
    
    while (failure==0):
      if (position+additional)>=0:
        try:
          #check for left edge
          for i in range (0,64,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
          
          if (failure != 1):
            #check for opposite end of board
            for i in range (56,64):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional+7
      
    failure = 0
    additional = 9
    
    while (failure==0):
      if (position+additional)>=0:
        try:
          #check for right edge
          for i in range (7,71,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
          
          if (failure != 1):
            #check for opposite end of board
            for i in range (56,64):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional+9
      
    failure = 0
    additional = -9
    
    while (failure==0):
      if (position+additional)>=0:
        try:
          #check for left edge
          for i in range (0,64,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
          
          if (failure != 1):
            #check for opposite end of board
            for i in range (0,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional-9
    
    failure = 0
    additional = -7
    
    while (failure==0):
      if (position+additional)>=0:
        try:
          #check for right edge
          for i in range (7,71,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
          
          if (failure != 1):
            #check for opposite end of board
            for i in range (0,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional-7
      
    failure = 0
    additional = 8
    
    while (failure==0):
      if (position+additional)>=0:
        try:
          
            #check for top of board
            for i in range (56,64):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional+8
      
    failure = 0
    additional = -8
    
    while (failure==0):
      if (position+additional)>=0:
        try:
          
            #check for bottom of board
            for i in range (0,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional-8
      
    failure = 0
    additional = -1
    
    while (failure==0):
      if (position+additional)>=0:
        try:
          
            #check for left of board
            for i in range (0,64,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional-1
      
    failure = 0
    additional = 1
    
    while (failure==0):
      if (position+additional)>=0:
        try:
          
            #check for right of board
            for i in range (7,71,8):
              if (position+additional == i):
                failure = 1
                if (board[position+additional] == 0):
                  output = output + [position+additional]
                  failure = 1
                elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                  output = output + [position+additional]
                  failure = 1
                  
              elif position == i:
                failure = 1
          
            if (failure != 1):
              if (board[position+additional] == 0):
                output = output + [position+additional]
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                failure = 1
              
        except:
          failure = 1
      else:
        failure = 1
      additional = additional+1
    
    return output 
    
  
    #white king
  if (board[position] == 15):   
    failure = 0
    additional = 7
    if (position+additional)>=0:
      
      try:
        #check for left edge
        for i in range (0,64,8):
          if (position+additional == i):
            failure = 1
            if (board[position+additional] == 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
              
          elif position == i:
              failure = 1
        
        if (failure != 1):
          #check for opposite end of board
          for i in range (56,64):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
        if (failure != 1):
          if (board[position+additional] == 0):
            output = output + [position+additional]
          elif (board[position+additional] >= 20):
            output = output + [position+additional]
            failure = 1
          elif (board[position+additional] < 20):
            failure = 1
            
      except:
        failure = 1
      
    failure = 0
    additional = 9
    if (position+additional)>=0:
    
      try:
        #check for right edge
        for i in range (7,71,8):
          if (position+additional == i):
            failure = 1
            if (board[position+additional] == 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
              
          elif position == i:
              failure = 1
        
        if (failure != 1):
          #check for opposite end of board
          for i in range (56,64):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
        if (failure != 1):
          if (board[position+additional] == 0):
            output = output + [position+additional]
          elif (board[position+additional] >= 20):
            output = output + [position+additional]
            failure = 1
          elif (board[position+additional] < 20):
            failure = 1
              
      except:
        failure = 1
      
    failure = 0
    additional = -9
    if (position+additional)>=0:
      try:
        #check for left edge
        for i in range (0,64,8):
          if (position+additional == i):
            failure = 1
            if (board[position+additional] == 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
              
          elif position == i:
              failure = 1
        
        if (failure != 1):
          #check for opposite end of board
          for i in range (0,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
        if (failure != 1):
          if (board[position+additional] == 0):
            output = output + [position+additional]
          elif (board[position+additional] >= 20):
            output = output + [position+additional]
            failure = 1
          elif (board[position+additional] < 20):
            failure = 1
            
      except:
        failure = 1
    
    failure = 0
    additional = -7
    if (position+additional)>=0:
  
      try:
        #check for right edge
        for i in range (7,71,8):
          if (position+additional == i):
            failure = 1
            if (board[position+additional] == 0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
              
          elif position == i:
              failure = 1
        
        if (failure != 1):
          #check for opposite end of board
          for i in range (0,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
        if (failure != 1):
          if (board[position+additional] == 0):
            output = output + [position+additional]
          elif (board[position+additional] >= 20):
            output = output + [position+additional]
            failure = 1
          elif (board[position+additional] < 20):
            failure = 1
            
      except:
        failure = 1
  

    failure = 0
    additional = 8
    if (position+additional)>=0:
  
      try:
        
          #check for top of board
          for i in range (56,64):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
              
      except:
        failure = 1
    
    failure = 0
    additional = -8
    if (position+additional)>=0:
    
      try:
        
          #check for bottom of board
          for i in range (0,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
            
      except:
        failure = 1
    
    failure = 0
    additional = -1
    if (position+additional)>=0:

      try:
        
          #check for left of board
          for i in range (0,64,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
            
      except:
        failure = 1

      
    failure = 0
    additional = 1
    if (position+additional)>=0:
    
      try:
        
          #check for right of board
          for i in range (7,71,8):
            if (position+additional == i):
              failure = 1
              if (board[position+additional] == 0):
                output = output + [position+additional]
                failure = 1
              elif (board[position+additional] >= 20):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0):
              output = output + [position+additional]
            elif (board[position+additional] >= 20):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] < 20):
              failure = 1
            
      except:
        failure = 1
    
    return output 
  
  
    #black king
  if (board[position] == 25):
    failure = 0
    additional = 7
    
    if (position+additional)>=0:

      try:
        #check for left edge
        for i in range (0,64,8):
          
          if (position+additional == i)and (position+additional)>=0:
            failure = 1
            if (board[position+additional] == 0)and (position+additional)>=0:
              output = output + [position+additional]
              failure = 1
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
              output = output + [position+additional]
              failure = 1
              
          elif position == i:
              failure = 1
        
        if (failure != 1):
          #check for opposite end of board
          for i in range (56,64):
            if (position+additional == i)and (position+additional)>=0:
              failure = 1
              if (board[position+additional] == 0)and (position+additional)>=0:
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10)and (position+additional)>=0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
        if (failure != 1):
          if (board[position+additional] == 0)and (position+additional)>=0:
            output = output + [position+additional]
          elif ((board[position+additional] < 20) and (board[position+additional] >= 10)and (position+additional)>=0):
            output = output + [position+additional]
            failure = 1
          elif (board[position+additional] >= 20):
            failure = 1
            
      except:
        failure = 1
      
      
    failure = 0
    additional = 9
 
    if (position+additional)>=0:
      try:
        #check for right edge
        for i in range (7,71,8):
          if (position+additional == i)and (position+additional)>=0:
            failure = 1
            if (board[position+additional] == 0)and (position+additional)>=0:
              output = output + [position+additional]
              failure = 1
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10)and (position+additional)>=0):
              output = output + [position+additional]
              failure = 1
              
          elif position == i:
              failure = 1
        
        if (failure != 1):
          #check for opposite end of board
          for i in range (56,64):
            if (position+additional == i)and (position+additional)>=0:
              failure = 1
              if (board[position+additional] == 0)and (position+additional)>=0:
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
        if (failure != 1):
          if (board[position+additional] == 0)and (position+additional)>=0:
            output = output + [position+additional]
          elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
            output = output + [position+additional]
            failure = 1
          elif (board[position+additional] >= 20):
            failure = 1
            
      except:
        failure = 1

      
    failure = 0
    additional = -9
    
    if (position+additional)>=0:
      try:
        #check for left edge
        for i in range (0,64,8):
          if (position+additional == i)and (position+additional)>=0:
            failure = 1
            if (board[position+additional] == 0)and (position+additional)>=0:
              output = output + [position+additional]
              failure = 1
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
              output = output + [position+additional]
              failure = 1
              
          elif position == i:
              failure = 1
        
        if (failure != 1):
          #check for opposite end of board
          for i in range (0,8):
            if (position+additional == i)and (position+additional)>=0:
              failure = 1
              if (board[position+additional] == 0)and (position+additional)>=0:
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
        if (failure != 1):
          if (board[position+additional] == 0)and (position+additional)>=0:
            output = output + [position+additional]
          elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
            output = output + [position+additional]
            failure = 1
          elif (board[position+additional] >= 20):
            failure = 1
            
      except:
        failure = 1
        
    failure = 0
    additional = -7
    
    if (position+additional)>=0:
      try:
        #check for right edge
        for i in range (7,71,8):
          if (position+additional == i)and (position+additional)>=0:
            failure = 1
            if (board[position+additional] == 0)and (position+additional)>=0:
              output = output + [position+additional]
              failure = 1
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
              output = output + [position+additional]
              failure = 1
              
          elif position == i:
              failure = 1
        
        if (failure != 1):
          #check for opposite end of board
          for i in range (0,8):
            if (position+additional == i)and (position+additional)>=0:
              failure = 1
              if (board[position+additional] == 0)and (position+additional)>=0:
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
        if (failure != 1):
          if (board[position+additional] == 0)and (position+additional)>=0:
            output = output + [position+additional]
          elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
            output = output + [position+additional]
            failure = 1
          elif (board[position+additional] >= 20):
            failure = 1
            
      except:
        failure = 1

      
    failure = 0
    additional = 8
    
    if (position+additional)>=0:
    
      try:
        
          #check for top of board
          for i in range (56,64):
            if (position+additional == i)and (position+additional)>=0:
              failure = 1
              if (board[position+additional] == 0)and (position+additional)>=0:
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0)and (position+additional)>=0:
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
            
      except:
        failure = 1
  
      
    failure = 0
    additional = -8
    
    if (position+additional)>=0:
 
      try:
        
          #check for bottom of board
          for i in range (0,8):
            if (position+additional == i)and (position+additional)>=0:
              failure = 1
              if (board[position+additional] == 0)and (position+additional)>=0:
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0)and (position+additional)>=0:
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
            
      except:
        failure = 1

      
    failure = 0
    additional = -1
    
    if (position+additional)>=0:

      try:
        
          #check for left of board
          for i in range (0,64,8):
            if (position+additional == i)and (position+additional)>=0:
              failure = 1
              if (board[position+additional] == 0)and (position+additional)>=0:
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0) and (position+additional)>=0:
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
            
      except:
        failure = 1
    
      
    failure = 0
    additional = 1
    
    if (position+additional)>=0:

      try:
        
          #check for right of board
          for i in range (7,71,8):
            if (position+additional == i) and (position+additional)>=0:
              failure = 1
              if (board[position+additional] == 0)and (position+additional)>=0:
                output = output + [position+additional]
                failure = 1
              elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
                output = output + [position+additional]
                failure = 1
                
            elif position == i:
              failure = 1
        
          if (failure != 1):
            if (board[position+additional] == 0)and (position+additional)>=0:
              output = output + [position+additional]
            elif ((board[position+additional] < 20) and (board[position+additional] >= 10) and (position+additional)>=0):
              output = output + [position+additional]
              failure = 1
            elif (board[position+additional] >= 20):
              failure = 1
            
      except:
        failure = 1
    
    return output 
  
    
def IsPositionUnderThreat(board,position,player):
  if board[position] == 0:
    print 'Empty spot.'
    return False
  else:
    if (player == 10):
      enemyPositions = GetPlayerPositions(board,20)
    elif (player == 20):
      enemyPositions = GetPlayerPositions(board,10)
    else:
      print 'Error, not a player (Enter 10 or 20).'
      return False
  
      
    for i in range (0,len(enemyPositions)):
      enemyMoves = GetPieceLegalMoves(board, enemyPositions[i])

      for j in range (0, len(enemyMoves)):
        if (enemyMoves[j] == position):
    
          return True
    
    return False 


#relative piece strengths
#pawn = +- 10
#knight = +-30
#bishop = +-30
#rook = +-50
#queen = +-90
#king = +- 900


#board evaluation
def boardScore (board):
  score = 0
  
  #white pawn value matrix 
  whitepawnmatrix = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0, 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0, 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5, 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0, 0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5, 0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
  
  #black pawn value matrix 
  blackpawnmatrix = list(reversed(whitepawnmatrix))

  #knight value matrix 
  knightmatrix = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0, -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0, -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0, -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0, -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0, -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0, -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0, -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
  
  #white bishop value matrix
  whitebishopmatrix = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0, -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0, -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0, -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0, -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0, -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0, -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0, -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
  
  #black bishop value matrix
  blackbishopmatrix = list(reversed(whitebishopmatrix))
  
  #white rook matrix
  whiterookmatrix = [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
  
  #black rook matrix
  blackrookmatrix = list(reversed(whiterookmatrix))
  
  #queen matrix
  queenmatrix = [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0, -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0, -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0, -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5, -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0, -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0, -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
  
  #white king matrix
  whitekingmatrix = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0, -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
  
  #black king matrix
  blackkingmatrix = list(reversed(whitekingmatrix))
  
  for i in range(0,64):
    if (board[i] == 10):
      score = score + 10 + whitepawnmatrix[63-i]
    elif (board[i] == 20):
      score = score - 10 - blackpawnmatrix[63-i]
    elif (board[i] == 11):
      score = score + 30 + knightmatrix[63-i]
    elif (board[i] == 21):
      score = score - 30 - knightmatrix[63-i]
    elif (board[i] == 12):
      score = score + 30 + whitebishopmatrix[63-i]
    elif (board[i] == 22):
      score = score - 30 - blackbishopmatrix[63-i]
    elif (board[i] == 13):
      score = score + 50 + whiterookmatrix[63-i]
    elif (board[i] == 23):
      score = score - 50 - blackrookmatrix[63-i]
    elif (board[i] == 14):
      score = score + 90 + queenmatrix[63-i]
    elif (board[i] == 24):
      score = score - 90 - queenmatrix[63-i]
    elif (board[i] == 15):
      score = score + 900 + whitekingmatrix[63-i]
    elif (board[i] == 25):
      score = score - 900 - blackkingmatrix[63-i]
      
  return score 
    

#function to generate new board from a potential move 
def generateBoardMove (board,initialposition,finalposition):
  newBoard = []
  for i in range (0,64):
    newBoard = newBoard + [board[i]]
  newBoard[finalposition] = board[initialposition]
  newBoard[initialposition] = 0
  return newBoard 


#chess player function 
def chessPlayer(board,player):
  
  status = False 

  if player == 10:
    enemy = 20
  elif player == 20:
    enemy = 10
  
  #make sure kings are still alive, otherwise no valid moves 
  kingpositioninitial = -1
  enemyking = -1
  for i in range (0,64):
    if board[i] == player+5:
      kingpositioninitial = i
    if board[i] == enemy+5:
      enemyking = i
      
  if kingpositioninitial == -1:
    #failure, player has already lost 
    status = False 
    print 'King is dead; Player',player,'lost.'
    return [False,[],[],[]]
    
  elif enemyking == -1:
    #failure, enemy has already lost 
    status = False
    print 'King is dead; Player',enemy,'lost.'
    return [False,[],[],[]]
    
  else:
    #the root node of the moves tree 
    moves = tree([0,0,0,board])
    
    #generate the evalTree (FIRST PARAMETER CONTROLS DEPTH OF GENERATION)
    moves = treeGenerator(2,board,player,moves)
    
    
    if player == 10:
      maximizingPlayer = True
    elif player == 20:
      maximizingPlayer = False
    
    
    level1minimax = minimax(moves,2,-9999,9999,maximizingPlayer)
    
    if maximizingPlayer == True:
      print 'Max:',level1minimax

    else:
      print 'Min:',level1minimax

    output = moves.Get_LevelOrder()
    
    #correlate the minimax index with the list of outputs to find which move is best, index+1 due to inclusion of initial state
    
    
    for i in range (0,len(moves.store[1])):
      if moves.store[1][i].store[0][2] == level1minimax:
        index = i
        break
      
    move = [output[index+1][0],output[index+1][1]]
    print move
    candidateMoves = []
    for i in range (1,len(moves.store[1])):
      newMove = [output[i][0],output[i][1]]
      moveScore = float(output[i][2])
      candidateMoves = candidateMoves + [[newMove,moveScore]]
    evalTree = output
    
    status = True
    
    finalOutput = [status,move,candidateMoves,evalTree]

    return finalOutput
    
    
    
    
#minimax with alpha-beta pruning 
def minimax(moves, depth, minimum, maximum, maximizingPlayer): 
  
  leaf = 0
  try: 
    #try to access the first child of the tree
    temp = moves.store[1][0]
  except:
    leaf = 1

  if depth == 0 or leaf == 1:
    #print '\nReached Leaf or depth bottom'
    #print 'score:', boardScore(moves.store[0][3]),
    #print 'for:', moves.store[0][0], moves.store[0][1]
    moves.store[0][2] = boardScore(moves.store[0][3])
    return moves.store[0][2]
    
  if maximizingPlayer == True:
    v = minimum
    #print 'calculating for maximizing'
    for i in range (0,len(moves.store[1])): 
      vnew = minimax(moves.store[1][i],depth-1,v,maximum,False)
      if vnew > v:
        v = vnew
      if v > maximum:
        return maximum
    moves.store[0][2] = v
    return v
    
  elif maximizingPlayer == False:
    v = maximum
    #print 'calculating for minimizing'
    for i in range (0,len(moves.store[1])):
      vnew = minimax(moves.store[1][i],depth-1,minimum,v,True)
      if vnew < v:
        v = vnew
      if v < minimum:
        return minimum
    moves.store[0][2] = v
    return v
  
  
def treeGenerator (depth,board,player,moves):
  if depth == 0:
    return moves
    
  positions = GetPlayerPositions(board,player)
  
  #determine friendly player and set enemy 
  if player == 10:
    enemy = 20
  if player == 20:
    enemy = 10
  
  #must return a un-check move if king is under threat 
  #first detect king
  kingpositioninitial = -1
  for i in range (0,64):
    if board[i] == player+5:
      kingpositioninitial = i
      
  if kingpositioninitial == -1:
    #failure, player has already lost 
    status = False 
    print 'King is dead; Player',player,'lost.'
    return moves

  
  #record possible moves for current player 
  #this stores the legal moves (final position)
  moves1 = []
  #this stores the piece associated with each move (initial position)
  pieces1 = []
  for i in range (len(positions)):
    moves1 = moves1 + [GetPieceLegalMoves(board,positions[i])]
    pieces1 = pieces1 + [positions[i]]
  #print 'All possible moves (no threat check):'
  #print moves1
  #print pieces1
  
  #fixes the moves and pieces lists to only have valid moves and pieces(king threat check)
  moves1final = []
  pieces1final = []
  for i in range (0,len(pieces1)):
    for j in range (0,len(moves1[i])):
      newBoard = generateBoardMove(board,pieces1[i],moves1[i][j])
      #print moves1[i][j]

      kingposition = -1
      for x in range (0,64):
        if newBoard[x] == player+5:
          kingposition = x
          

      if kingposition != -1:
        if IsPositionUnderThreat(newBoard,kingposition,player) == True:
          #print 'The king position at threat is',kingposition
          pass
        
        #elif IsPositionUnderThreat(newBoard,moves1[i][j],player) == True:
          #print 'Move makes piece under threat. Do not Move.'
          #pass
        
        else:
          moves1final = moves1final + [moves1[i][j]]
          pieces1final = pieces1final + [pieces1[i]]
  
  #print 'Potential Moves/Initial positions for',
  #print player
  #print moves1final
  #print pieces1final
  
  #this stores the first level of boards 
  boards1 = []
  #generate a board for each potential move
  for i in range (0,len(pieces1final)):

    newBoard = generateBoardMove(board,pieces1final[i],moves1final[i])
    
    score = 0
    #print score
    boards1 = boards1 + [[pieces1final[i],moves1final[i],score,newBoard]]
    
  #for i in range(0,len(boards1)):
    #print boards1[i]
  
  #add to the tree
  for i in range(0,len(boards1)):
   
    addedTree = tree(boards1[i])
    addedTree = treeGenerator(depth-1,boards1[i][3],enemy,addedTree)
    moves.AddSuccessor(addedTree)
    
  return moves
  
  

#must import these later from chessPlayer_tree.py 
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
    

#relative piece strengths
#pawn = +- 10
#knight = +-30
#bishop = +-30
#rook = +-50
#queen = +-90
#king = +- 900

#White: Offset=10
#Black: Offset=20

#Piece: Value
#Pawn:   +0
#Knight: +1
#Bishop: +2
#Rook:   +3
#Queen:  +4
#King:   +5

def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1

def genBoard():
   r=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63

      r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
      r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
      r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*3] = i+getPiece("king")
      else:
         r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*4] = i+getPiece("king")

      for j in range(0,8):
         r[shift+factor*(j+8)] = i+getPiece("pawn")
   
         
   return r

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum

board=genBoard()

#board[9] = 12
#board[16] =21
#board[18] =22
#board[24] = 23

#board[36]= 10
#board[43] = 23
#board[51] = 25
#board[60] = 20
#board[6] = 15

newBoard = board

print printBoard(newBoard)

player = 20
answer = 'y'

while answer == 'y':

  try:
    if player == 10:
      player = 20
    elif player == 20:
      player = 10

    output = chessPlayer(newBoard,player)
    newBoard = generateBoardMove(newBoard,output[1][0],output[1][1])
    print printBoard(newBoard)
    print '\n'

  except:
    print 'Game over.'
  answer = raw_input()
  if answer != 'y':
    break



