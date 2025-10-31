#tuple:-tuple as a fixed,unchangeable sequence of data.
#properties of tuple:-
#1.Orderd:-the items have a defined order,and that order is preserved.
#2.Immutable:-once created ,we cannot change,add,or remove items in tuple.
#3.Heterogeneous:- tuples can contain items of different data types(strings,intergers,floats,even other lists or objects)
empty_tuple = ()
print(f"Empty tuple:{empty_tuple}")               #output = Empty tuple :()
#A tuple of integers:-
num = (1,2,3,4,5,6)
print(num)                                         #output = (1,2,3,4,5,6)
#A tuple of strings:-
fruits = ("apple","banana","fig","mango")
print(fruits)                                    #output = ('apple','banana','fig','mango')
print(fruits[3])                                 #output = mango
# A tuple of mixed data types:-
mixed = (12,3.14,"hello",False) 
print(mixed)                                   #output = (12,3.14,'hello',False)
#A tuple containing a list(nested mutable object):-
nested_tuple = (1,"world",[1,2,4,[7,8]])
print(nested_tuple[-1][-1][0])                                  #output = (1,'world',[1,2,4,[7,8]])
#important point:-
#A single -element tuple requires a trailing comma(,) without it,python treats its as just the item itself,not tuple.
single_tuple = (5)
print(type(single_tuple))                       #output = <class 'int'>
single_tuple = (5,)
print(type(single_tuple))                       #output = <class 'tuple'>
#Accessing elements using positive indexing:-
my_tuple = ("a","b","c","d")
print(my_tuple[0])                             #output = a
print(my_tuple[3])                              #output = d
#Accessing elements using negative indexing:-
my_tuple = ("a","b","c","d")
print(my_tuple[-1])                            #output = d
print(my_tuple[-3])                            #output = b
#slicing:-
numbers = (1,2,3,4,5,6,7,8,9)
print(numbers)                                   #output = (1,2,3,4,5,6,7,8,9)
print(numbers[2:8])                              #output = (3,4,5,6,7,8)
print(numbers[:5])                               #output = (1,2,3,4,5)
print(numbers[2:8:2])                            #output = (3,5,7)
print(numbers[5:])                                #output = (6,7,8,9)
print(numbers[::-1])                             #output = (9,8,7,6,5,4,3,2,1)
# OPERATION OF TUPLE:-
#1.Concatenation:-
tuple1 = (1,2)
tuple2 = (3,4)
tuple3 = tuple1+tuple2
print(tuple3)                                       #output = (1,2,3,4)
#2.Repetition:-
tuple1= (2,1)
tuple2 = tuple1*4
print(tuple2)                                       #output = (2,1,2,1,2,1,2,1)
#3.Membership:-
my_tuple = (1,3,5,7,9)
print(1 in my_tuple)                              #output = true
print(3 not in my_tuple)                          #output = false
#tuple packing(it means creating a tuple without parantheses):-
packed_tuple = "hello",24,True
print(packed_tuple)                 #output = ('hello',24,True)
#tuple unpacking(the numbers of variables on the left must match the number of elements in the tuple.)
X,Y,Z= "seema",20,"jaipur"
print(f"X ={X},Y ={Y},Z ={Z}")               #output= X=seema,Y=20,Z=jaipur
#unpacking tuple with *(star operator):-
data = (1,2,3,4,5,6,7)
x,y,*rest, =data
print(f"x={x},y={y},rest={rest}")             #output = x=1,y=2,rest=[3,4,5,6,7]
x,y,*rest,z = data
print(f"x={x},y={y},rest={rest},z={z}")          #output = x=1,y=2,rest =[3,4,5,6],z=7
#swapping using tuple unpacking:-
a=30
b=20
(b,a)
a,b = 20,30
print(f"a={a},b={b}")                        #output = a=20,b=30

my_list = [1,2,3,4]
my_tuple = tuple(my_list)
print(type(my_tuple))                       #output = <class 'tuple'>


my_tuple = (1,2,3,4)
my_list = list(my_tuple)
print(type(my_list))                       #output = <class 'list'>
#methods of tuple:-
#1.count:-
data =(1,3,2,3,4,5,3,6,3)
print(data.count(3))                   #output =4
#2.index:-
data = (1,3,2,3,4,5,3,6,3)
print(data.index(3))                 #output = 1
print(data.index(3,2))               #output = 3














