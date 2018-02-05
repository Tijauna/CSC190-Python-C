def f(n):
  if n<100:
    return 89
  elif n == 100:
    return 42
  elif n>= 100:
    while(n>100):
      n = n/2 + 1
    return n
  else:
    return 99
    
