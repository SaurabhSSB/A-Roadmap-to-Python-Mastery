class Entry:
    def __init__(self, roll_no, name):
        self.roll_no= roll_no
        self.name= name
    def show(self):
        print(f"Roll No.:- {self.roll_no} and Name {self.name}")

class Course(Entry):
    # INHERITANCE
    def show(self):
        print(f"Roll No.:- {self.roll_no} and Name {self.name} has done BTech in Computer Science")


a=Entry(10, "Saurabh Singh Bhandari")
a.show()
b=Course(11, "Nittin")
b.show()

class Entry:
    def __init__(self, roll_no, name):
        self.roll_no= roll_no
        self.name= name
    def show(self):
        print(f"Roll No.:- {self.roll_no} and Name {self.name}")

class Course(Entry):
    # INHERITANCE
    def show(self):
        print(f"Roll No.:- {self.roll_no} and Name {self.name} has done BTech in Computer Science")
        super().show()
        # The super() keyword in Python is used to refer to the parent class


class Computer_lab(Entry):
    def __init__(self, roll_no, name, language):
        super().__init__(roll_no, name)
        self.language= language

a=Entry(10, "Saurabh Singh Bhandari")
a.show()
b=Course(11, "Nittin")
b.show()
c=Computer_lab(23,"Chaya" , "Java")
print(c.language)


