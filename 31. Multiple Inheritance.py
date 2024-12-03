# Multiple Inheritance
class Entry:
    def __init__(self, roll_no, name):
        self.roll_no= roll_no
        self.name= name
    def open(self):
        print(f"{self.name} Rollno. {self.roll_no} is eligible for admission")
    def approved(self):
        print(f"{self.name} is approved and is given Entry.")

class Stream:
    def __init__(self, name, age, stream):
        self.name= name
        self.age= age
        self.stream= stream
    def open(self):
        print(f"{self.name} age {self.age} is eligible for {self.stream} in BTech")
    def approved(self):
        print(f"{self.name} is approved in this Stream.")

class Library (Stream, Entry):
    def __init__(self, roll_no, name, stream):
        super().__init__(roll_no, name)
        self.stream= stream
    def open(self):
        print(f"{self.name} Rollno. {self.roll_no} of {self.stream} Stream is eligible to take books from here.")

a= Entry(10,"Saurabh Singh Bhandari")
b= Stream("Saurabh Singh Bhandari", 22, "Computer Science")
c= Library(10,"Saurabh Singh Bhandari", "Computer Science")
a.open()
b.open()
c.open()
c.approved()