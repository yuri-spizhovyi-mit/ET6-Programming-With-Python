def search(L, e):
  for i in range(len(L)):
    if L[i] == e:
      return True
    if L[i] > e:
      return False
  return False

L = [1, 2, 3, 4]
e = 5

print(search(L, e))
