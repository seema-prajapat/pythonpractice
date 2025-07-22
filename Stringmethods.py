#string methods:- In python strings have a varitey of built-in methods.we use the (.) operator to call a method in python.
#1. upper():- this method converts the string in a uppercase.
A= "seema"
print(A.upper())       #output= SEEMA
#2. lower():-  this method converts the string in a lowercase.
A= "SEEMA"
print(A.lower())        #output= seema
#3. Strip():-this method removes leading and trailing whitespace.
A= "--seema-prajapat--"
print(A.strip("-"))       #output = seema-prajapat
print(A.rstrip("-"))      #output = --seema-prajapat
print(A.lstrip("-"))     #output = seema-prajapat--
#4.replace(old,new):- this method replace the string occurance of a substring.
str = "Hello miss"
print(str.replace("miss", "mister"))  #output = Hello mister
print(str.replace("H","W"))           #output = wello miss
#5.split():- splits the string into lists based on delimiter(default is whitespace)
str = "My name is seema prajapat."
print(str.split())          #output = ['My', 'name', 'is', 'seema', 'prajapat.']
str = "17/7/2025"
print(str.split("/"))       #output = ['17', '7', '2025']
#6.join():- joins elements of an iterable (like a list) into a single string,with a specified separator.
str = ['My', 'name', 'is', 'seema', 'prajapat.']
print("" .join(str))          #output = Mynameisseemaprajapat.
print(" " .join(str))          #output = My name is seema prajapat.
str = ['17', '7', '2025']      #output = 17-7-2025
print("-".join(str))
#7. find():-  this method returns the index of the first occurrence of a substring(or -1 if not found)
str = "Hello world"
print(str.find("l"))          #output = 2
print(str.find("s"))          #output = -1 
#8.count = this method counts the occurrence of substring in the string.
str = "Hello world"
print(str.count("l"))       #output = 3