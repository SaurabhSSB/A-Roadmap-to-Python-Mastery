'''
Object- Oriented Programming in Python is to use classes and objects to represent real- world concepts and entities.
Object- Oriented Programming is used to map real world entities.
Entry- Class/ Blue- Print/ Template- Properties and methods that an object in class will have
Students- Object/ Entity- Instance of Class- contains it's own data and methods
'''
class Student:
    roll_no= 10
    name= "Saurabh Singh Bhandari"
    graduation= "BTech"
    def info(self):
        print(f"Roll No. {self.roll_no} name is {self.name} he has a {self.graduation} degree")

x= Student()
x. name= "Nittin"
x. roll_no= 16
x.info()