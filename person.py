class person:
    def __init__(self,name,age):
        self.name=name # self.name stores the name 
        self.age=age # self.age stores the age
    def great(self):
        print(f'Hello, my name is {self.name} and I am {self.age}years old')

individual1 = person('cyber',13)
individual2 = person('cruz',17)
individual3 = person('ben',15)
individual4= person('chriba',19)
individual5 = person('cythia',16)

individual1.great()
individual2.great()
individual3.great()
individual4.great()
individual5.great()

def age(self):
    if age >= 18:
        return True
    else:
        return False