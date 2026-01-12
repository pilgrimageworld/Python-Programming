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

class Order: 
    def __init__(self, name, price): 
        self.name = name
        self.price = price

    def __gt__(self, odr): 
        return self.price > odr.price

odr1 = Order("Chips", 20)
odr2 = Order("Tea", 15)

if(odr1 > odr2):
    print("Order 1 is expensive than Order 2")
else: 
    print("Order 2 is expensive than Order 1")
        