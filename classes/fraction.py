class Fraction(object):
  def __init__(self, numer, denom):
    self.numer = numer
    self.denom = denom

  def __str__(self):
    return str(self.numer) + ' / ' + str(self.denom)
  
  def get_numer(self):
    return self.numer
  
  def get_denom(self):
    return self.denom
  
  def __add__(self, other):
    numer_new = other.get_denom() * self.get_numer() + other.get_numer() * self.get_denom()
    denom_new = other.get_denom() * self.get_denom()
    return Fraction(numer_new, denom_new)
  
  def __sub__(self, other):
    numer_new = other.get_denom() * self.get_numer() - other.get_numer() * self.get_denom()
    denom_new = other.get_denom() * self.get_denom()
    return Fraction(numer_new, denom_new)
  def convert(self):
    return self.get_numer() / self.get_denom()


one_half = Fraction(1, 2)
two_third = Fraction(2, 3)
three_quarters = Fraction(3, 4)
#print(one_half + two_third)
second_new = two_third - three_quarters
print(second_new.convert())
