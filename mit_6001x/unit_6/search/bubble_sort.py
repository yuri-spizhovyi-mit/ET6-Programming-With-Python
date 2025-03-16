def bs(L):
  swap = 1
  while swap > 0:
    swap = 0
    for i in range(len(L) - 1):
      if L[i] > L[i + 1]:
        temp = L[i]
        L[i] = L[i + 1]
        L[i + 1] = temp
        swap += 1
      
  return L
L = [3, 2 ,1, 1, 2, 3]
print(bs(L))
