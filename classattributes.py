class Dog:
    species = "js"
    def __init__(self ,name,age):
        self.Dog_name = name
        self.Dog_age = age
        self.is_hungry = True
    def bark(self):
        print(f"{self.Dog_name} says woof!")  
    def eat(self):
        if self.is_hungry:
            print(f"{self.Dog_name}is eating..")  
            self.is_hungry = False  
        else:
            print(f"{self.Dog_name} is not hungry right now.")    
my_dog = Dog("tommy",3)      
my_dog.bark() 
my_dog.eat() 
my_dog.eat()    
your_dog = Dog("puffy",5)  
your_dog.species = "lebra dog"    
your_dog.bark() 
your_dog.eat() 
#access instance attributes:
print(f"My dog name is {my_dog.Dog_name} and he is {my_dog.Dog_age} months old") 
print(f"My dog name is {your_dog.Dog_name} and he is {your_dog.Dog_age} months old")
#access class attributes:
print(f"tommy is the memeber of {my_dog.species} species")
print(f"puffy is the memeber of {your_dog.species} species")


        