def intersect(L1, L2):
  tmp = []
  for e1 in L1:
    for e2 in L2:
      if e1 == e2:
        tmp.append(e1)
  res = []
  for e in tmp:
    if e not in res:
      res.append(e)
  return res, tmp

L1 = [1, 2, 3]
L2 = [1, 2, 2, 4]
print(intersect(L1, L2))
