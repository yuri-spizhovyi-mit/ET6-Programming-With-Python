def fib_recur(n):
  """Assume n an int >=0"""
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib_recur(n-2) + fib_recur(n-1)
  
print(fib_recur(7))
