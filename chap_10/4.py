import math as m
class calculator:
    def __init__(self, number):
        self.number = number
    
    def square(self):
        return self.number**2
    
    def cube(self):
        return self.number**3
    
    def sqRoot(self):
        return m.sqrt(self.number)
    
    @staticmethod
    def greet():
        print("Hello")

a = calculator(4)
print(a.square())
print(a.cube())
print(a.sqRoot())
a.greet()