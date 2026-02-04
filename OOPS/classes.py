#OOPS: Object Oriented programming is the part of programming languages that allows us to structure the code 
#in the terms of classes and objects for better organisation and reusability.

#Class: An class is basically defining how an object should look like . It is a blueprint or creating the objects.
#Example Class: Fruits  Objects: Mango, Banana, Apple, Orange 
#Object:
#__init__: the init is basically a constructor that is used to inistailize the objects. It is used to assign properties and to perform operations when necessary.
#The self parameter is a reference to the current instance of the class
#It is used to access properties and methods that belong to the class.self can be named anything not necessarily to be named as self.
#Methods are functions that are created in classes.

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

#Q4) Create a class student.

class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

student1 = student("Eshaan",21,95)
print(student1.name)
print(student1.age)
print(student1.marks)

#Q5)Delete the age property

class human:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

h1 = human("Eshaan",21)
print(h1.name,h1.age )

del h1.age
#print(h1.name,h1.age)

#Q6) Modify the exiting properties of the class

class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

h1 = human("Eshaan",21)
print(h1.age,h1.name)

h1.age = 20
print(h1.name,h1.age)

#Q6)Class property vs instance property

class person:
    species = "human"
    def __init__(self,gender):
        self.gender = gender
p1 = person("female")
p2 = person("male")
print(p1.gender)
print(p2.gender)


"""class Dog: creates a class named Dog, which acts as a blueprint for dog objects.
species is a class attribute, meaning it is shared by all instances of the class.
__init__() is a constructor method that runs automatically when a new object is created. It is used to initialize object data.
self refers to the current object, allowing each object to store and access its own data.
self.name and self.age are instance attributes, unique to each Dog object created from the class."""

#Q7)Create a simple class with methods

class person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello, My name is"+ self.name)

p1 = person("Emily")
p1.greet()

#Q8) Create a calculator using OOPS Concepts

class calculator:
    def add(self,a,b):
        return a+b
    
    def multiply(self,a,b):
        return a*b
    
calc = calculator()
print(calc.add(5,15))
print(calc.multiply(5,4))

#Q9)How do we access the methods ?

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())


#Q10)Create a playlist where we can add songs, delete songs and view songs

class playlist:
    def __init__(self,name):
        self.name = name 
        self.songs = []

    def add_songs(self,song):
        self.songs.append(song)
        print(f"added{song}")

    def delete_songs(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"removed {song}")
    
    def show_songs(self):
        print(f"playlist'{self.name}':")
        for song in self.songs:
            print(f"-{song}")

my_playlist = playlist("Favorites")
my_playlist.add_songs("Bohemian Rhapsody")
my_playlist.add_songs("Stairway to Heaven")
my_playlist.show_songs()

#Q12)1️⃣ Book Library Create a class Library where you can:add books,remove books,view all books

class library:
    def __init__(self,name):
        self.name = name
        books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Book added {book}")

    def delete_book(self,book):
        for book in self.books:
            self.books.remove(book)
            print(f"Book removed {book}")

    def show_books(self):
        print(f"Library'{self.name}':")
        for book in self.books:
            print(f"-{book}")

#Inheritance:This is the property of a class where once class can extract the property of the other class or in formal terms inherit the properties.
#Parent class: The class from which the property is inherited is called as parent
#Child class: The class which inherits the property from another class is called as child class

class animal:
    def eat(self):
        print("dog is eating")

    def drink(self):
        print("dog is drinking")

class Dog(animal):
    def bark(self):
        print("dog is barking")

d1 = Dog()

d1.eat()
d1.drink()
d1.bark()


class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   
        self.age = age

#super() keyword is used to call the parents class methods from the child class.

c = Child("Eshaan", 21)
print(c.name)   



class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print("The vehicle is starting.")

class Car(Vehicle):
    def __init__(self,brand,model):
        self.model = model
        super().__init__(brand)

    def details(self):
        print(f"The car has started and is of the {self.brand} and {self.model}")

c1 = Car("Toyota","Innova")
c1.start()
c1.details()
print(c1.brand)
print(c1.model)


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name:{self.name} , Age:{self.age}")

class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name)
        super().__init__(age) #super().__init__(name,age)
        self.subject = subject

    def teach(self):
        print(f"Teaching {self.subject}")

class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name)
        super().__init__(age)
        self.grade = grade

    def study(self):
        print(f"studying in grade {self.grade}")

t1 = teacher("Mr. Sharma", 40, "Maths")
s1 = student("Eshaan", 21, "Final Year")

t1.introduce()
t1.teach()

s1.introduce()
s1.study()


    




