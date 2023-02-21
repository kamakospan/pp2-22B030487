class Person:
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def printyear(self): # prints out the year they were born
    print(2023 - self.age)
  def printnameage(self):
    print(self.firstname, self.age)
    

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe", 45)
x.printyear()