class Student:
    School= "Kendriya Vidyalaya"
    def __init__(self, roll_no, name):
        self.roll_no= roll_no
        self.name= name
    
    def show(self):
        print(f"Name {self.name} Roll No.{self.roll_no} studied at {Student.School}")

    @classmethod
    def change(cls, School):
        cls.School = School

Student.change("PM Shri")
a= Student(10, "Saurabh Singh Bhandari")
a.show()
print(Student.School)

# Class Method as Alternative Constructor

class Student:
  def __init__(self, name, roll_no):
    self.name = name 
    self.roll_no = roll_no
    
  @classmethod
  def fromStr(cls, data):
    return cls(data.split(",")[0], int(string.split(",")[1]))
    
e1 = Student("Harry", 12000)
print(e1.name)
print(e1.roll_no)

string = "John,12000"
e2 = Student.fromStr(string)
print(e2.name)
print(e2.roll_no)
