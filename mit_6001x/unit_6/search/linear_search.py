def linear_search(L, e):
  count = 0
  found = False
  for i in range(len(L)):
    count += 1
    if e == L[i]:
      found = True
      break
  return found, count

L = [1, 2, 3, 4]
e = 4

print(linear_search(L, e))
