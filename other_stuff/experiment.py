# Inner and Outer Classes

# class Outer: 
#     def __init__(self):
#         print("This is Outer Class Construtor")

#     def start(self):
#         print("This is start method of outer")

#     class Inner: 
#         def __init__(self, outer):
#             self.outer = outer
#             print("This is Inner Class Constructor")

#         def start(self):
    
#             print(f"This is start method of inner {self.outer}")
        

# out1 = Outer()
# out1.start()
                

# inn1 = Outer.Inner(outer=out1)
# inn1.start()


# class Car: 
#     def __init__(self, brand , model):
#         self.brand = brand
#         self.model = model
#         self.engine = self.Engine()

#     class Engine: 
#         def __init__(self):
#             self.status = "Off"


#         def start(self): 
#             self.status = "Running"
#             print("Engine Started")

#         def stop(self): 
#             self.status = "Off"
#             print("Engine stopped")

#     def drive(self): 
#         if self.engine.status == "Running": 
#             print(f"Driving the {self.brand} {self.model}")
#         else: 
#             print("Start the engine first!")

    
# car = Car("Toyoto", "Corolla")

# car.drive()

# car.engine.start()

# car.drive()


# Inheritance


# class Person: 
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def display_name(self):
#         print(f"First Name: {self.first_name}\nLast Name: {self.last_name}")


# class Student(Person):
#     def __init__(self, f_name, l_name):
#         super().__init__(self, f_name, l_name) 


        

# student1 = Student("Shakib", "Ansari")

# student1.display_name()


# Getter and Setter


class Person: 
    def __init__(self):
        self._age = 0
    
    @property
    def age(self): 
        return self._age
    
    @age.setter
    def age(self, new_age): 
        if new_age < 18:
            raise ValueError("Sorry, Your Age is Below Eligiiblity")
        
        self._age = new_age


p1 = Person()

p1.age = 15

print(p1.age)
        