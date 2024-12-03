# 2 types of Constructors- Parameterized and Default

class Student:
    def __init__(self, a, b, c):
        self.roll_no= a
        self.name= b
        self.graduation= c
    def info(self):
        print(f"Roll No. {self.roll_no} name is {self.name} he has a {self.graduation} degree")

x= Student( 10, "Saurabh Singh Bhandari", "BTech")
y= Student( 16, "Nittin", "BTech")
x.info()
y.info()

# Instance & Class Variable

class Student:
    School= "Kendriya Vidyalaya" # Class Variable
    Student_no= 0 
    def __init__ (self, roll_no,name):
        self.roll_no= roll_no
        self.name= name
        self._class= 12 # Instance Varaible
        Student.Student_no+= 1
    def show(self):
        print(f"{self.name} Roll No.{self.roll_no} School {Student.School} once studied in {self._class} class in {self.School}")

a= Student(10, "Saurabh Singh Bhandari")
print(Student.School)
a.show()
print(f"Total Student enrolled= {Student.Student_no}")