'''
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside 
of class while implementing the concepts of inheritance.
Three Types:-
Public access modifier
Private access modifier
Protected access modifier
'''
# Public 
class Student:
    def __init__(self,roll_no, name, graduation):
        self.roll_no= roll_no
        self.name= name
        self.graduation= graduation
    def info(self):
        print(f"Roll No. {self.roll_no} name {self.name} has a {self.graduation} degree")

x= Student(10, "Saurabh Singh Bhandari", "BTech")
x.info()

# Private
class Student:
    def __init__(self,roll_no, name, graduation):
        self.roll_no= roll_no
        self.__name= name
        self.graduation= graduation
    def info(self):
        print(f"Roll No. {self.roll_no} name {self.__name} has a {self.graduation} degree")

x= Student(10, "Saurabh Singh Bhandari", "BTech")
x.info()
print(x._Student__name) # Name Mangling

# Protected Access Modifier
class Student:
    def __init__(self,roll_no, name, graduation):
        self.roll_no= roll_no
        self._name= name
        self.graduation= graduation
    def info(self):
        print(f"Roll No. {self.roll_no} name {self._name} has a {self.graduation} degree")

x= Student(10, "Saurabh Singh Bhandari", "BTech")
x.info()
print(x._name) # Name Mangling

print(x.__dir__())