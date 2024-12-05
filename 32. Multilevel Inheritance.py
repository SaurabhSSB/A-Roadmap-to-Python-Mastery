class Entry:
    Entrance= "Permitted"
    def __init__(self, name, qualification):
        self.name=name
        self.qualification=qualification
    def open(self):
        print(f"{self.name} has done {self.qualification} and is {Entry.Entrance}")

class Class(Entry):
    def __init__(self, roll_no, name, course):
        Entry.__init__(self, name, qualification= "Twelfth")
        self.roll_no= roll_no
        self.course= course
    def open(self):
        #Entry.open(self)
        print(f"{self.name} Rollno. {self.roll_no} has done {self.qualification} and is going to enroll in {self.course}")


class Stream(Class):
    def __init__(self, roll_no, name, stream):
        Class.__init__(self, roll_no, name, course= "Btech")
        self.stream= stream
    def open(self):
        Class.open(self)
        print(f"{self.name} of Rollno. {self.roll_no} from {self.course} is opting for {self.stream}")

a= Stream( 10, "Saurabh Singh Bhandari", "Computer Science")
a.open()

c= Class(10, "Saurabh Singh Bhandari", "BTech")
c.open()
b=Entry("Saurabh", "Twelfth")
b.open()

print(Class.mro())