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


#Abstraction is the process in which we hide the working details of the algorithm.
# It plays a crucial role in building scalable, mantainable and modular codes.
#abstraction in its essence is about hiding the complexity and showing the most simplest interface possible.

from abc import ABC, abstractmethod

#In python we ise this library to import abstract classes and methods

#In Python, the @abstractmethod decorator is a tool used in abstract base classes (ABCs) to define methods that must be implemented by subclasses

# Example 

from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    class car(vehicle):
        def move(self):
            print("The car is moving")

    class boat(vehicle):
        def move(self):
            print("The boat is moving")


from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def paymentmethods(self,amount):
        pass

class CreditCardPayment(payment):
    def paymentmethods(self,amount):
        print("The amount is paid through credit card")

class UPIpayments(payment):
    def paymentmethods(self,amount):
        print("The amount is paid using UPI")


payment1 = CreditCardPayment()
payment1.paymentmethods(500)

payment2 = UPIpayments()
payment2.paymentmethods(300)


#Q)
"""
Abstraction Coding Question

Design a system for different notification services.

Requirements:

Create an abstract class Notification.

Define an abstract method send(message).

Create two subclasses:

EmailNotification

SMSNotification

Each subclass should implement the send() method in its own way.
"""
from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass

class EmailNotification(Notification):
    def send(self,message):
        print(f"This is the notification sent through email: {message}")

class SMSNotification(Notification):
    def send(self,message):
        print(f"This is the message sent through sms:{message}")

message1 = EmailNotification()
message1.send("Hi User")

message2 = SMSNotification()
message2.send("Hi User. How was your experience ?")

#Q)
"""
Abstraction Coding Question (Level-Up)

Design a system for different file storage services.

Requirements:

Create an abstract class StorageService.

Define two abstract methods:

upload(file_name)

download(file_name)

Create two concrete classes:

LocalStorage

CloudStorage

Each class should implement both methods in its own way.

Write client code that:

Uploads a file

Downloads the same file

Use polymorphism (i.e., store objects in a list of StorageService).

Expected Output (example):
Uploading report.pdf to local storage
Downloading report.pdf from local storage
Uploading report.pdf to cloud storage
Downloading report.pdf from cloud storage

Rules (gym-boss rules 💪):

No class nesting

Method names and parameters must match exactly

Use ABC and @abstractmethod

Client code should not depend on concrete class names
"""

from abc import ABC,abstractmethod

class StorageService(ABC):
    @abstractmethod
    def upload(self,file_name):
        pass

    @abstractmethod
    def download(self,file_name):
        pass

class LocalStorage(StorageService):
    def upload(self,file_name):
        print(f"Uploading {file_name} to local storage")

    def downlaod(self,file_name):
        print(f"downloading {file_name} from local storage")

class CloudStorage(StorageService):
    def upload(self,file_name):
        print(f"Uploading {file_name} to cloud storage")

    def download(self,file_name):
        print(f"Downloading {file_name} from clound storage")


s1 = CloudStorage()
s1.download("Marks.csv")

s2 = LocalStorage()
s2.upload("Marks.csv")
#using polymorphism
#It refers to the ability of an entity to perform different actions at different times based on the action to be performed is called as polymorphism

services = [LocalStorage(),CloudStorage()]

for service in services:
    service.upload("Marks.csv")
    service.download("Marks.csv")



#Encapsulation

#Encapsulation means hiding the internal details of the a class and only exposing what is needed.
#It helps protecting the data from being change directly and keeps the code secured and organised.

#Example:
class Employee:
    def __init__(self,name,salary):
        self.name = name          #public attribute 
        self.__salary = salary    #Private attribute

emp = Employee("Eshaan",3000000)
print(emp.name)
print(emp.salary) #this will raise an error as a private attribute cannot be accessed from outside the class.

#ACCESS SPECIFIERS

"""
Public 
Private 
Protected
"""

class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible


class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass

class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly




#Self Test (Questions generated by GPT's)
'''
Q1)Design an abstract class PaymentGateway with an abstract method pay(amount).

Create two concrete classes:

CardPayment

UPIPayment

Write code to:

Call pay() using a base class reference

Show how abstraction helps here'''
from abc import ABC,abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CardPayment:
    def pay(self,amount):
        print(f"This amount is paid using Card:{amount}")

class UPIPayment:
    def pay(self,amount):
        print(f"This amount is paid using UPI:{amount}")
p1 = CardPayment()
p1.pay(600)

p2 = UPIPayment()
p2.pay(690)


'''
Create a class Employee with:

attributes: name, salary

method: get_bonus()

Create a subclass Manager that:

overrides get_bonus()

gives 20% bonus instead of default 10%

Demonstrate overriding with objects.'''

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary  = salary

    def get_bonus(self):
        print(f"Got a bonus of {(self.salary*10)/100}")
        
class Manager(Employee):
    def get_bonus(self):
        print(f"Got a bonus of {(self.salary*20)/100}")




class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
        print(f"The amount deposited is {amount}.")

    def withdraw(self,amount):
        if self.amount>self.__balance:
            print("The amount trying to be withdrawn is greater than the balance of the account. Try with a lower amount")
        else:
            self.__balance -= amount
            print(f"The withdraw of the amount was successful:{amount}")


#Q4)
'''
Polymorphism Without Inheritance

Create two classes:

EmailNotification

SMSNotification

Both should have a method send(message).

Write a function notify(notification_obj) that works for both classes
👉 No inheritance allowed.'''

class EmailNotification:
    def send(self, message):
        print(f"Email sent: {message}")

class SMSNotification:
    def send(self, message):
        print(f"SMS sent: {message}")

def notify(notification):
    notification.send("Hello")

notify(EmailNotification())
notify(SMSNotification())




#Q5) Identify the bug and fix
'''
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")
        super.start()
'''

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")
        super().start()


#Q6)
from abc import ABC, abstractmethod

class logger(ABC):
    @abstractmethod
    def log(self,message):
        pass

class FileLogger:
    def log(self,message):
        print(f"This using FileLogger {message}")

class ConsoleLogger:
    def log(self,message):
        print(f"This is using ConsoleLogger {message}")

Loggers = [FileLogger(),ConsoleLogger()]

for Logger in Loggers:
    Logger.log("Hi")
