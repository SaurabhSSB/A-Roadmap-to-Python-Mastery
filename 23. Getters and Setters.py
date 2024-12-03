# Python program showing a use 
# of get() and set() method in 
# normal function 
  
class Geek: 
    def __init__(self, age = 0): 
         self._age = age 
      
    # getter method 
    def get_age(self): 
        return self._age 
      
    # setter method 
    def set_age(self, x): 
        self._age = x 
  
raj = Geek() 
  
# setting the age using setter 
raj.set_age(21) 
  
# retrieving age using getter 
print(raj.get_age()) 
  
print(raj._age) 

# Python program showing a 
# use of property() function 

class Geeks: 
	def __init__(self): 
		self._age = 0
	
	# function to get value of _age 
	def get_age(self): 
		print("getter method called") 
		return self._age 
	
	# function to set value of _age 
	def set_age(self, a): 
		print("setter method called") 
		self._age = a 

	# function to delete _age attribute 
	def del_age(self): 
		del self._age 
	
	age = property(get_age, set_age, del_age) 

mark = Geeks() 

mark.age = 10

print(mark.age) 

# Python program showing the use of 
# @property 

class Geeks: 
	def __init__(self): 
		self._age = 0
	
	# using property decorator 
	# a getter function 
	@property
	def age(self): 
		print("getter method called") 
		return self._age 
	
	# a setter function 
	@age.setter 
	def age(self, a): 
		if(a < 18): 
			raise ValueError("Sorry you age is below eligibility criteria") 
		print("setter method called") 
		self._age = a 

mark = Geeks() 

mark.age = 19

print(mark.age) 

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a positive integer")
        self._age = age
        
'''
In object-oriented programming, setter and getter methods are used to control access to an object's properties. 
Getters are used to access the value of an object's properties. Used to return the value of a specific property and 
conventionally defined with @property decorator.
We need Setters which can be added by decorating method with @property_name.setter, this is done because getters do not take any 
parameters and we cannot set the value through getter method. 
the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.

Getters and Setters in python are often used when:
- We use getters & setters to add validation logic around getting and setting a value.
- To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

Encapsulate data: Hide internal implementation details.
Validate input: Ensure data integrity.
Provide flexibility: Allow for future modifications without affecting external code.
Readability: Well-defined getter and setter methods can improve code readability and maintainability.

Explanation:

Private Attributes:
Attributes prefixed with an underscore (_) are conventionally treated as private. This indicates that they should be accessed and modified only through the defined methods.
Getter Methods:

These methods return the value of a private attribute.
get_name() and get_age() are examples of getter methods.

Setter Methods:
These methods set the value of a private attribute.
set_name() and set_age() are examples of setter methods.
The set_age() method demonstrates input validation.

In Conclusion, Getters are a convenient way to access the values of an object's properties, while keeping the internal representation
of the property hidden. This can be useful for data encapsulation and data validation. 
'''

class MyClass:
    def __init__(self,value):
          self. _value= value
    def show(self):
          print(f"{self._value} is a private attribute, thus we are using setter and getter to get access to it.")
                  
    @property
    def value(self):
          return(self._value)
      
    @value.setter
    def value(self,value):
          self._value= value
            
a= MyClass(11)
a.show()
a.value= 5
print(a.value)
a.show()