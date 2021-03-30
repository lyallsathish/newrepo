# I am witing a code in this file
class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
class MyClass(Student):
  pass
s1 = student("lyall",20)
s2 = MyClass("aksh",19)
print(s1.name)
print(s1.age)
