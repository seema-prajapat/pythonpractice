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