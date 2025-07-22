str = input("Enter the string")
index = 0
upper = 0
lower = 0
digits = 0
special = 0
while index < len(str):    
    char = str[index]
    if char == "#":
        break
    elif char.isupper():
        upper += 1
    elif char.islower():
        lower += 1  
    elif char.isdigit():
        digits += 1
    else:
        special += 1  
    index += 1    
print("uppercase letters.", upper) 
print("lowercase letters.",lower) 
print("digits." , digits)  
print("special character.",special)       
