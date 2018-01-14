# coding: utf-8
class stack:
  def __init__(self):
    self.store = []
    self.length = 0
          
  def push(self, value):
    self.store = self.store + [value]
    self.length = self.length + 1
    
  def pop(self):
    if self.length == 0:
      return False
    returnValue = self.store[self.length-1]
    del self.store[self.length-1]
    self.length = self.length - 1
    return returnValue
