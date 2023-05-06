class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#this will also return false because it is referring to an object that is made from a class with a __len__ function that returns 0 or False: