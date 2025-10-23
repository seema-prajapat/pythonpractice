def cal():
    while True:
        print("select operation.no1.add no2.subtract no3. multiplication no4.division")
        choice = input("Enter choice(1/2/3/4):")
        number1 = float(input("Enter first number:"))
        number2 = float(input("Enter second number:")) 
        if choice == "1":
            print(f"{number1}+{number2} = {number1+number2}")
        elif choice == "2":
            print(f"{number1}-{number2} = {number1-number2}")  
        elif choice == "3":
            print(f"{number1}*{number2} = {number1*number2}")  
        elif choice == "4":
            print(f"{number1}/{number2} = {number1/number2}") 
        else:
            print("Invalid choice.")
        next_cal = input("Do next calculation?(yes/no):").lower()
        if next_cal != "yes":
            break
cal()                




    