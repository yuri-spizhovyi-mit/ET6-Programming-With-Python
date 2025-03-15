def is_subset(L1, L2):
  for e1 in L1:
    matched = False
    for e2 in L2:
      if e1 == e2:
        matched = True
        break
    if not matched:
      return False
  return True


L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 2, 4]
print(is_subset(L1, L2))
