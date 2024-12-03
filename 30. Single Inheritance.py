# Single Inheritance
class Entry:
    def __init__(self,roll_no, name, stream):
        self.roll_no= roll_no
        self.name= name
        self.stream= stream
    def open(self):
        print(f"{self.name} Rollno.{self.roll_no}is s student of {self.stream} in BTech")

class Python(Entry):
    def __init__(self, roll_no, name, age):
        Entry.__init__(self, roll_no, name, stream= "Computer Science")
        self.age= age
    def open(self):
        print(f"{self.name} Rollno. {self.roll_no} of {self.stream} of {self.age} age in BTech is eligible for Python Workshop")

a= Entry(10, "Saurabh Singh Bhandari", "Computer Science")
b= Python(11, "SaurabhSSB", 22)
a.open()
b.open()