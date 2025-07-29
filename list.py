#list:- lists are the most fundamental and versatile data structure in python.they are ordered,mutable (changeable) sequence of items.
# in the list each item has a specific position,called an index.
#In list we use [] square brackets.
#List has 3 properties:-
#1.Ordered:- In the list the items have a defined order,and that order will not change.
#2.Mutable:- In list we can change ,add or remove items after the list has been created.
#3.Haterogeneous:-Lists can contain items of different data types(integers,strings,float,even other lists or objects).
abc = ["seema",20,"jaipur",303603,[1,3,5,[1,2,[1,0,4,5]]]]
print(abc)                                 #output = ["seema",20,"jaipur",303603,[1,3,5]]
print(abc[3])                              #output = 303603
print(abc[4][2])                           #output = 5
print(abc[0][3])                           #output = m
print(abc[0].upper())                      #output = SEEMA
print(abc[4][3][1])                        #ouput = 2
print(abc[4][3][2][1])                     #output = 0
#slicing:-
num = [1,2,3,4,5,6,7,8,9]
print(num[0:])                       #output = [1,,2,3,4,5,6,7,8,9]
print(num[3:7])                       #output = [4,5,6,7]
print(num[0:8:3])                      #output = [1,4,7]
print(num[::-1])                       #output = [9,8,7,6,5,4,3,2,1]
#reference variable:-
a =["varsha" ,1,3,5,7]
b = a
b[0] = "Seema"
print(a,b)
#element change
fruit = ["apple","orange","fig","grapes"]
fruit[3] = "mango"
print(fruit)                          #output = ['apple','orange','fig','mango']
fruit = ["apple","orange","fig","grapes"]
fruit[1:3] =["banana","date"]
print(fruit)                            #output = ['apple','banana','date','grapes']