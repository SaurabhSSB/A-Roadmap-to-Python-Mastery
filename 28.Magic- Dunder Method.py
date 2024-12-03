'''
These are special methods that we can define in our classes, and when invoked, they give us a powerful way to 
manipulate objects and their behaviour.
'''

class Student:
    def __init__(self,name):
        self.name=name
   
    def __len__(self):
        x=0
        for i in self.name:
            x+= 1
        return x
    
    def __str__(self):
        return f"Student {self.name}"
    
    def __repr__(self):
        return f"Student('{self.name}')"
    
    def __call__(self):
        print("SaurabhSinghBhandariSSB")

a= Student("Saurabh Singh Bhandari")
print(len(a))
print(str(a))
print(repr(a))
a()

# Operator Overloading
class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k) 
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))