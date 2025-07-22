while True:
    word = input("Enter the word:")
    if word.lower() == "exit":
        break
    if word == word[::-1]:
        print("word is a palindrome.")
    else:
        print("word is not a palindrome.")    