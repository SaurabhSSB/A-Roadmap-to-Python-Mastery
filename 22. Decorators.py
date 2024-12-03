def decorate(fx):
    def mfx(*args,**kwargs):
        '''*args= argument as tuple, **kwargs= argument as dictionary as key- value pairs'''
        print("your choice has been registered")
        fx(*args,**kwargs)
        print("Thanks a lot!")
    return(mfx)


@decorate
def check():
    print("Only for Demo")

def alternative():
    print("Only as an Alternative")

def add(a,b):
    print(a + b)

@decorate
def product(a,b):
    print(a * b)

def remainder(a,b):
    print(a / b)

def difference(a,b):
    print(a - b)

check()

decorate(alternative)()
decorate(add)(5,6)

product(2,4)