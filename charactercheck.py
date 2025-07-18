vowels="aeiouAEIOU" 
char=input("Enter a single letter:")
if len(char) !=1 or not char.isalpha():
    print("Invalid character.")
elif char in vowels:
    print("It's a vowel.") 
else:
   print("It's a consonant.")    

  
     