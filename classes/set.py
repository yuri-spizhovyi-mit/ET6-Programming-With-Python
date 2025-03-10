class IntSet(object):
  def __init__(self):
    """Create an empty set of integers"""
    self.vals = []
  def insert(self, e):
    """Assumes e is an integer and inserts e into self""" 
    #if e not in self.vals:
    self.vals.append(e)
  def member(self, e):
    """Assumes e is an integer
      Returns True if e is in self, and False otherwise"""    
    return e in self.vals
  def remove(self, e):
    try:
      self.vals.remove(e)
    except:
      raise ValueError(str(e) + ' not found')
  def __str__(self):
      self.vals.sort()
      result = ""
      for e in self.vals:
        result = result + str(e) + ',' 
      return '{' + result[:-1] + '}'
  
  def intersect(self, other):
      common_elements = IntSet()
      for e in self.vals:
        if e in other.vals:
          common_elements.insert(e) 
        return common_elements

  def __len__(self):
        return len(self.vals)


s1 = IntSet()
s2 = IntSet()
s1.insert(3)
s1.insert(4)
s2.insert(3)
s2.insert(5)


print(s1.intersect(s2))
