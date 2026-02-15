# class Student: 
#     name = "Shakib Ansari"

# s1= Student()
# print(s1.name)

# print(s1)

# class Mobile: 
#     def __init__( name, model, price): 
#         self.name = name
#         self.model = model
#         self.price = price
    

# mob1 = Mobile("", "OPPO", "F7", 27999.00)


# print("Mobile Name: ", mob1.name, "\nMobile Model: ", mob1.model, "\nMobile Price: ", mob1.price)

# class Student:

#     college_name = "SDGI"

#     # def hello_everyone

#     def welcome_student(self):
#         print("Welcome to",self.name )

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    


# s1 = Student("Shakib", 98)
# s1.welcome_student()


# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Student: 
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def print_marks_average(self):
#         sum = 0
#         for val in self.marks: 
#             sum += val
#         return sum/3
    
#     @staticmethod
#     def hello():
#         print("Hello")


# s1 = Student("Shakib", [89, 87, 90])
# print(s1.print_marks_average())

# s1.hello()

# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

# class Account:
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no
    
#     def debit(self, amount):
#         self.balance = self.balance - amount
    
#     def credit(self, amount):
#         self.balance = self.balance + amount
    
#     def print_balance(self):
#         print("You have ", self.balance)

# acc = Account(2300, 12344321)

# acc.print_balance()
# acc.debit(10000)
# acc.print_balance()
# acc.credit(100)
# acc.print_balance()

# class Student: 
#     def __init__(self, name):
#         self.name = name


# s1 = Student("Shakib")

# print(s1.name)
# del s1.name

# print(s1)
# print(s1.name)

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

    
# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.__acc_pass)

# class Car: 

#     def __init__(self, type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("Car Start")
#     def stop():
#         print("Car Stop")

    
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name


# car1 = ToyotaCar("Fortuner", "Electric")

# print(car1.name)
# print(car1.type)


# class Person:
#     name = "Anonymous"

#     @classmethod
#     def changeName(cls, name): 
#         cls.name = name

    

# p1 = Person()
# p1.changeName("Shakib")
# print(p1.name)
# print(Person.name)


# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem 
#         self.math = math
        # self.percentage = str((self.phy+self.chem+self.math)/3) + "%"
    
    # def calcPercentage(self):
        # self.percentage = str((self.phy+self.chem+self.math)/3) + "%"


#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3) + "%"


# s1 = Student(78, 98, 77)

# print(s1.percentage)

# s1.chem = 87
# print(s1.chem)
# print(s1.percentage)


# class Complex: 
#     def __init__(self, real, img): 
#         self.real = real
#         self.img = img

#     def showNumber(self): 
#         print(self.real,"i +", self.img, "j")

#     def __add__(self, num2): 
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)


# num1 = Complex(3, 5)
# num2 = Complex(5, 6)

# num1.showNumber()
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()


# Define a Circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


# class Circle: 
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 22/7*self.radius**2  # Tr^2

#     def perimeter(self): 
#         return 2 * 22/7 * self.radius # 2Tr

# c1 = Circle(8)

# print(c1.area())
# print(c1.perimeter())
    

# class Employee: 
#     def __init__(self, role, dept, salary): 
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self): 
#         print("Employee Name: ", self.name)
#         print("Employee Age : ", self.age)
#         print("Employee Role: ", self.role)
#         print("Employee Dept: ", self.dept)
#         print("Employee Salary: ", self.salary)



# class Engineer(Employee): 
#     def __init__(self, name, age, role, dept, salary): 
#         super().__init__(role, dept, salary)
#         self.name = name 
#         self.age = age


# engineer1 = Engineer("Shakib", 19, "Software Developer", "Engineering", 76899.000)

# engineer1.showDetails()


# Create a class called Order which stores item & its price. Use Dunder function __gt__() to convey that: order1 > order2 if price of order1 > price of order2

# class Order: 
#     def __init__(self, name, price): 
#         self.name = name
#         self.price = price

#     def __gt__(self, odr): 
#         return self.price > odr.price

# odr1 = Order("Chips", 20)
# odr2 = Order("Tea", 15)

# if(odr1 > odr2):
#     print("Order 1 is expensive than Order 2")
# else: 
#     print("Order 2 is expensive than Order 1")
        

# class Dog: 
#     species = "Cannie"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# d1 = Dog("Tom", 4)

# # print(f"Dog Name: {d1.name}\nDog Age: {d1.age}\nDog Species: {d1.species}")

# # print(f"Dog Species access using Class: ", Dog.species)

# print("Dog 1 Species: ", d1.species)
# print("Dog Species: ", Dog.species)

# d2 = Dog("Buddy", 3)
# d2.species = "German Shephard"

# print("Dog 2 Species: ", d2.species)

# print("Dog 1 Species: ", d1.species)
# print("Dog Species: ", Dog.species)


# print("This is last species: ", d2.species)

# Dog.species = "Something New"

# print("Dog Species: ", Dog.species)
# print("Dog 1 Species: ", d1.species)
# print("Dog 2 Species: ", d2.species)


# Inheritance

# class Dog: 
#     def __init__(self, name) :
#         self.name = name

#     def display_name(self):
#         print(f"Dog's Name: {self.name}")
        
# class Labrador(Dog):
#     def sound(self):
#         print("Labrador woofs")

# class GuideDog(Labrador):
#     def guide(self):
#         print(f"{self.name}Guides the way")


# class Friendly: 
#     def greet(self):
#         print("Friendly")

# class GoldenRetriever(Dog, Friendly): 
#     def sound(self): 
#         print("Golden Retriever Barks")

#     def somthing(self):
#         print("Something")

# dog1 = Dog("Tommy")
# dog1.display_name()
        
# dog2 = Labrador("Netiz")
# dog2.display_name()
# dog2.sound()

# dog3 = GuideDog("Max")

# dog3.display_name()
# dog3.sound()
# dog3.guide()

# dog4 = GoldenRetriever("Charlie")
# dog4.display_name()
# dog4.sound()
# dog4.greet()

# print(GoldenRetriever.mro())

# Multiple Inheritance - Diamond Problem

# class A: 
#     def show(self): 
#         print("A's show method")

# class B(A): 
#     def show(self):
#         print("B's show method")

# class C(A): 
#     def show(self):
#         print("C's show method")


# class D(B, C): 
#     pass

# obj = D()

# obj.show()
# print(D.mro())

# Polymorphism - Compile Time

# class Calculator: 
#     def add(self, *args):
#         return sum(args)

# cal = Calculator()

# print(cal.add(10, 20, 40))
# print(cal.add(10.2, 20, 30.4))
# print(cal.add("Hello ", "My ", "Name ", "is ", "ShAn"))


# def add(itr): 
#     result = itr[0]
#     for i in itr[1:]:
#         result += i

#     return result

# print(add(["Hello ", "My ", "Name ", "is ", "ShAn"]))

# Polymorphism - Run Time

# class Animal: 
#     def speak(self): 
#         return "Animal Speak"


# class Dog(Animal): 
#     # 1. Method Overriding
#     def speak(self): 
#         return "Woof!!!"

# # 2. Duck Typing
# class Cat: 
#     def speak(self): 
#         return "Meaw"
    
# print(Animal().speak())
# print(Dog().speak())

# def make_animal_speak(animal): 
#     return animal.speak()

# print(make_animal_speak(Cat()))


# 3. Operator Overloading

# class Vector: 
#     def __init__(self, x, y) :
#         self.x = x
#         self.y = y

#     def __add__(self, other): 
#         return Vector(self.x + other.x ,self.y + other.y)
    
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"

# v1 = Vector(2, 3)
# v2 = Vector(4, 5)

# v3 = v1+v2

# print(v3)


# Encapsulation

# class Dog: 
#     def __init__(self, name, breed, age):
#         self.name = name # Public Attribute
#         self._breed = breed # Protected Attribute
#         self.__age = age

#     # Public Method
#     def get_info(self): 
#         return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

#     # Getter and Setter for Private Attribute

#     def get_age(self): 
#         return self.__age
    
#     def set_age(self, age): 
#         if age > 0: 
#             self.__age = age
#         else:
#             print("Invalid Age")
        
# dog = Dog("Buddy", "Labrodar", 3)

# print(dog.name)
# print(dog._breed)

# print(dog.get_age())

# dog.set_age(5)
# print(dog.get_age())


# Encapsulation

from abc import ABC, abstractmethod

class Dog(ABC): # Abstract Method
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def display_name(self): 
        print(f"Dog's Name: {self.name}")

class Labrador(Dog): # Partial Abstraction
    def sound(self): 
        print("Labrador Woof!")

class Beagle(Dog): 
    def sound(self):
        print("Beagle Bark!")


dogs = [Labrador("Buddy"), Beagle("Charlie")]

for dog in dogs: 
    dog.display_name()
    dog.sound()


