#class:- A class is a blueprint or a template for creating objects.
# In python,a class defines the attributes (data)and methods(behaviors)that all objects of that class will share.
#Attributes:-these are the data or properties of an object.ex(for car class attributes could be color,brand,and milage).
#Methods:- these are the functions that an object can perform.ex(for a car class,methods could be strat_engine(),drive()).

#class defining:-we can define a class using the class keyword,
# followed by the class name(which,by convention,should start with capital letter).
class Socialmedia:
    CEO = "mark"
    def like():
        print("liked")
    def comment():
        print("commented")    
print(Socialmedia.CEO)
Socialmedia.like() 
Socialmedia.comment()
#creating objects from a class:-
class Car:
    color = "blue"
    brand = "royals roy"
    milage = "3mph"
    def engine(self):
        print("RR engine")
    def drive(self):
        print("driving")   
    def honk(self):
        print("peeeee") 
a = Car()
b = Car() 
print(a)   
print(b) 
b.brand = "Tata" 
b.color = "white"    
print(a.brand)
print(a.color)
print(b.brand)
print(b.color)
print(a.honk())
#Attributes:- attributes are the data or properties associated with an object.
#they store the information about a specific instance.
# think of them as variables that belong to an object.

#Methods:-methods are the functions that belong to a class they define the behaviors or actions an object can perform.
       

