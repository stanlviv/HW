class Person:
    def __init__(self,name,age):
        self.name = str(name)
        self.age = int(age)
        self.info= "{}s age is {}".format(name, age)