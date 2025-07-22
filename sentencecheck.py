while True:
    sentence = input("Enter a sentence:")
    if sentence.strip().lower() == "stop": 
     break
    wordcount = len(sentence.split())
    if wordcount > 5:
       print("long sentence.")
    else:
       print("short sentence.")   
