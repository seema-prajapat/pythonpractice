import os 
while True:
    command = input("-->")
    if command == "ls":
        print(os.listdir())
    elif command == "lsfolder":
       item = os.listdir() 
       for x in item:
        if   
