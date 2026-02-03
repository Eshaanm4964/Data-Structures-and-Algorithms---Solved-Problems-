#OOPS: Object Oriented programming is the part of programming languages that allows us to structure the code 
#in the terms of classes and objects for better organisation and reusability.

#Class: An class is basically defining how an object should look like . It is a blueprint or creating the objects.
#Example Class: Fruits  Objects: Mango, Banana, Apple, Orange 
#Object:
#__init__: the init is basically a constructor that is used to inistailize the objects. It is used to assign properties and to perform operations when necessary.

#Q1)Create a class named Person, use the __init__() method to assign values for name and age:
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = person("Eshaan",20)
print(person1.name,person1.age )

#Q2)Create a class without __init__

class person():
    pass

p1 = person()
p1.name = "Eshaan"
p1.age = "21"

print(p1.name)
print(p1.age)

#Q3) Create a class named dog with the class attribute called as species.
class dog:
    species ="canine"

    def __init__(self,name,age):
        self.name = name
        self.age = age 

dog1 = dog("German Shephard",3)
print(dog1.name)
print(dog1.age)

"""class Dog: creates a class named Dog, which acts as a blueprint for dog objects.
species is a class attribute, meaning it is shared by all instances of the class.
__init__() is a constructor method that runs automatically when a new object is created. It is used to initialize object data.
self refers to the current object, allowing each object to store and access its own data.
self.name and self.age are instance attributes, unique to each Dog object created from the class."""