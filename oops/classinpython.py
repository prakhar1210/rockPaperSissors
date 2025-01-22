class Dog:
    kingdom = "Animal"

    """User defined object to represent and manage dog data"""
    def __init__(self, name, age, breed):
        # instace attributes

        self.name = name
        self.age = age
        self.breed = breed
        pass

    def describe(self):
        """describe the dog"""
        return f"{self.name} is a {self.age} year old {self.breed}"
    
dog1 = Dog("Dodo", 7,"Lab")
dog2 = Dog("Warner", 3, "lab")

print(dog1.name)
print(dog1.age)
print(dog1.breed)
print(dog1.kingdom)

print(dog2.describe())
print(dog1.describe())


print(type(Dog))

class Students:
    """User defined data structure for the students in a class or school"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):

        return f"{self.name}'s age is {self.age}."



class Red(Students):
    def house(self, house="Red"):
        return "{} is in {} house.".format(self.name, house)

class Blue(Students):
    def house(self, house="Blue"):
        return "{} is in {} house.".format(self.name, house)  
# class Red(Students):
#     def house(self, house="Red"):
#         return "{} is in {} house".format(self.name, house)
#     # pass

# class Blue(Students):
#     def house(self, house="Blue"):
#         return "{} is in {} house".format(self.name, house)
#     #  pass

    
student1 = Blue("Prakhar Shrivastava", 10)
student2 = Red("Saras Ajay Shrivastava", 12)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)

print(student1)
# print(student2.describe())
print(type(student1))
print(isinstance(Red, Students))
print(student1.house())

dog1.name = "Blacky"

dog1.breed = "Desi"
print(dog1.name)
print(dog1.breed)
print(dog1.describe())