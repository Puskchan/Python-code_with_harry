class Programmer():
    company = "Microsoft"
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    

harsh = Programmer("harsh", 100, 22)
kriti = Programmer("kriti", 250, 30)
print(harsh.age)
print(kriti.salary)
harsh.company = "Google"
print(harsh.company)    
print(kriti.company)    
