class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        #FILL THIS IN
        self.keys = []
        self.values = []

        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        #FILL THIS IN
        if k not in self.keys:
            self.keys.append(k)
            self.values.append(v)
        else:
            ind = self.keys.index(k)
            self.values.pop(ind)
            self.values.insert(ind, v)
            
        
    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN
        if k in self.keys:
            ind = self.keys.index(k)
            return self.values[ind]
        else:
            raise KeyError
        
        
    def delete(self, k):
        """ k, immutable object """   
        #FILL THIS IN
        if k in self.keys:
            ind = self.keys.index(k)
            self.keys.pop(ind)
            self.values.pop(ind)
        else:
            raise KeyError
md = myDict()   
md.assign(1,2)       
md.assign(2,3) 
print(md.getval(1))
print(md.getval(2))
md.delete(1) 
print(md.getval(1))
