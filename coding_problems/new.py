class Custom:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self, name):
        return name
    
    def get_slaary(self):
        return self.salary
    

cus = Custom('Asim', 85000000)

print(cus.get_name('Asim'))
print(cus.salary)


