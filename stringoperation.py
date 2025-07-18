#string operations:
#1.concatenation:- we can combine two or more strings using the oprator(+).
A="Seema"
B="Prajapat"
C=A+B
print(C)              #Output= Seemaprajapat
#2.Repetition:-we can repeat  a string multiple time using  thr oprator(*).
A="*"
B=8
C=A*B
print(C)               #output= ********
#3.Indexing:- In the string each character has a index number.which strats from (0).
A="Shyam"
print(A[4])             #Output = m
print(A[0])             #Output = S
print(A[-2])            #Output = a
#4.Slicing:- We can extract the strings into substrings by using slicing.
A="Seema"
print(A[1:])             #output = eema
print(A[1:4])            #output = eem
print(A[0:4:2])          #output = Se

A="0123456789"
print(A[0:10])             #output = 0123456789
print(A[2:10:3])          #output = 258
print(A[::-3])            #output = 9630
print(A[-7:2:-2])          #output = 3
#4.length:- we can get the length of string using the Len() function.
A = "Amanprajapat"
print(len(A))             #output = 12
#5.Membership:- we can check that a substring is exists in a string using (in or not in)operation.
str = "India"
print("I" in str)         #output = true
print("N" in str)         #output = false
#6. manipulation:- strings are immutable.
str = "Radha"
str = "w"+ str[1:]        #output = wadha
print(str)