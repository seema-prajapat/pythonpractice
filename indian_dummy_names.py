indian_dummy_names = [
    "Aarav Sharma", "Veda Iyer", "Ishaan Patel", "Saanvi Kapoor", "Aditya Reddy",
    "Ananya Gupta", "Vikram Mehta", "Priya Rao", "Arjun Desai", "Neha Verma",
    "Rohit Singh", "Sneha Joshi", "Karan Shah", "Pooja Malhotra", "Sameer Agarwal",
    "Shreya Jain", "Rahul Yadav", "Kritika Choudhury", "Amit Kumar", "Rina Nair",
    "Ravi Mishra", "Tanya Kapoor", "Manish Gupta", "Swati Sharma", "Vishal Bhat",
    "Ayesha Khan", "Deepak Patil", "Tanvi Agarwal", "Siddharth Reddy", "Aarti Mehta",
    "Ankur Prasad", "Madhavi Rao", "Puneet Sharma", "Maya Verma", "Anil Kapoor",
    "Disha Patel", "Yash Rajput", "Kiran Das", "Divya Joshi", "Rajesh Saini",
    "Pallavi Singh", "Raghav Gupta", "Simran Bedi", "Nikhil Deshmukh", "Kavya Saxena",
    "Himanshu Kumar", "Neelam Kapoor", "Gaurav Tiwari", "Rekha Yadav", "Suman Nair"
]
#1.count total number of names in the list:-
print(len(indian_dummy_names))           #output = 50


#2.print all the names in capital letters:-
for name in indian_dummy_names:
    print(name.upper())

#3. print all the names start with "A" in the list:-
for name in indian_dummy_names:
    if name.startswith("A"): 
     print(name)
     
#4.print all the names strat with "y" in the list:-    
for name in indian_dummy_names:
   if name.startswith("Y"):
    print(name)                               #output = yash rajput

#5.print all the names ends with the "a" in the list:-
for name in indian_dummy_names:
   if name.endswith("a"):
      print(name)

#6. print the all surnames in the list:-
for name in indian_dummy_names:
   for word in name.split():
      if word  != name.split()[0]:
         print(word)
         print(word.upper())
        
   










