#write a function to display days in month.
# ask the user to input a month(1-12)and print how many days are in that month(consider leap year for february).
def days_in_month():
    month=int(input("Enter a month(1-12):"))
    year = int(input("Enter a year:"))
    if month in [1,3,5,7,8,10,12]:
       print("31 Days")
    elif month in[4,6,9,11]:
        print("30 Days")  
    elif month == 2:
      if(year % 4==0 and year % 100 != 0):
        print("29 Days")
      else:
       print("28 Days")     
    else:
       print("Invalid month")
days_in_month()
#write a function to display leap year checker.
#ask the user to input a year and determine whether it is a leap year  or not.
def leap_year():
    Year = int(input("Enter a year:"))
    if (Year % 4 == 0 and Year % 100 !=0 or Year % 400 == 0):
       print("Year is a leap year.")
    else:
       print("Year is not a leap year.")  
leap_year()   
#write a function display evenly divisible.
#ask the user for a number and check if its divisible by both 4 and 6.
def evenly_divisible():
   num = int(input("Enter a number:"))
   if num % 4 == 0 and num % 6 == 0:
     print(f"{num} is divisible by both 4 and 6.")
   else:
     print(f"{num} is not divisible by both 4 and 6.")   
evenly_divisible()  

#Write a function to display Time of Day Greeting
#Ask the user to enter the time (in hours) and print a greeting based on the time of day:
#morning(5 PM - 12 PM )
#Afternoon (12 PM - 5 PM)
#Evening (5 PM - 9 PM)
#Night (9 PM - 5 AM)
def day_greeting():
   hour = int(input("Enter the hour of the day:"))
   if 5 <= hour < 12:
    print("Good morning.")
   elif 12 <= hour < 16:
    print("Good afternoon.")
   elif 16 <= hour < 20:
    print("Good evening.")   
   elif (20 <= hour < 24) or ( 0 <= hour < 5):
    print("Good night.")     
   else:
    ("Invalid hour")   
day_greeting()   

#Write a function to display the sum of the first 10 natural numbers.  
def natural_number_sum():
  total = sum(range(1,11))
  print(total)
natural_number_sum() 

#write a function to display print even numbers from  to 10.
def even_number():
  for x in range(2,11,2):
    print(x)
even_number()

#Write a function to display print numbers in a countdown from 10 to 1.
def countdown():
  for x in range(10,0,-1): 
   print(x)
countdown() 
 
#Write a function to display Character Case Checker
#Take a single character from the user and check if it's an uppercase letter, a lowercase letter, or not a letter at all.
def upperlower():
   char = input("Enter a single letter:")
   if char.isupper():
     print("uppercase.")
   elif char.islower():
     print("lowercase.")       
   else:
      print("invalid letter.") 
upperlower()      

      

  
   
