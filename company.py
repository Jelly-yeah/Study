class Employee(object):
    def __init__(self, name):
        self.name = name

    def _salary(self):
        print("I have salary.")

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)

    def _salary(self):
        print("My salary is $15000 .")

class Programmer(Employee):
    def __init__(self, name, hours):
        super().__init__(name)
        self.hours = hours

    def _salary(self):
        print("My salary is ${} .".format(150*self.hours))
        
class Seller(Employee):
    def __init__(self, name, money):
        super().__init__(name)
        self.money = money

    def _salary(self):
        print("My salary is ${}  .".format(int(0.05*self.money+1200)))

M = Manager("ZhangSan")
M._salary()
P = Programmer("LiSi", 160)
P._salary()
S = Seller("WangWu", 100000)
S._salary()
