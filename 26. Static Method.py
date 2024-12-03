class Calci:
    def __init__(self, a):
        self.num= a
    
    def add(self, b):
        self.num= self.num+ b
    
    @staticmethod
    def product(x,y):
        return(x*y)
    
a= Calci(10)
print(a.num)

a.add(15)
print(a.num)

b= Calci.product(3,5)
c= a.product(5,5)
print(b,c)