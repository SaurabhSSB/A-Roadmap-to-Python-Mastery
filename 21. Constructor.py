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