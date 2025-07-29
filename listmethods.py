#list Methods:-
#1.append():- this method add the data in end of list.
student = ["seema","shweta","nisha","komal"]
student.append("pihu")
print(student)                                   #output = ['seema','shweta','nisha,'komal','pihu']

#2.insert():- this method add the data in list by indexing value.
fruits =["apple","date","blueberry","banana"]
#fruits.insert(2,"fig")    
# print(fruits)                                #output = ['apple', 'date', 'fig', 'blueberry', 'banana']
#fruits.insert(-11,"grape")
#print(fruits)                                  #output = ['grape','apple','date','blueberry','banana']    
fruits.insert(-1,"grape")
print(fruits)                                #output = ['apple', 'date', 'blueberry', 'grape', 'banana']
#if we give the invalid nagative index value in insert method of list then it will add the data on the 0 (zero) index..
#if we give the valid nagative index value in insert method of list then it will add the data auto +1 for ex:-(-1,"x")
# it will add the data on -2 index

#3.remove():- this methode remove the give data from list..
fruits =["apple","date", "banana","blueberry","banana"]
fruits.remove("blueberry")
print(fruits)                                #output = ['apple', 'date', 'banana']
fruits.remove("banana")
print(fruits)                                #output =['apple','date','blueberry','banana']
#if we have duplicate data in list then remove method will remove only first occurance....

#4.pop():- this method removes the data from the end of the list and also remove by using indexing value..
number = [1,2,3,4,5]
number.pop()
print(number)                            #output = [1,2,3,4]
number = [1,2,3,4,5,6,7]
number.pop(5)
print(number)                               #output = [1,2,3,4,5,7]
#5.sort():- this method arrange the list in the ascending order or descending order.
num =[4,8,2,7,1,6,0]
num.sort()
print(num)                          #output = [0,1,2,4,6,7,8]
name =["seema","ritika","riteka","pooja"]
name.sort()
print(name)                          #output = ['pooja', 'riteka', 'ritika', 'seema']
name =["seema","ritika","riteka","pooja"]
name.sort( reverse=True)
print(name)                           #output = ['seema', 'ritika', 'riteka', 'pooja']
#sorted() function:-
list =[1,5,0,8,3,9,7,2]
sortedlist =sorted( list)
print(sortedlist)                    #output = [0,1,2,3,5,7,8,9]
print( f" original list after sorted():{list}") #output =[1,5,0,8,3,9,7,2]
#.6 count():-
number =[1,2,2,2,3,4,5,2,6,7,7,8]
print(number.count(2))                       #output = 4
print(number.count(5))                         #output = 1
print(number.count(27))                         #output = 0
#7.index():-
number =[1,2,2,2,3,4,5,2,6,7,7,8]
print(number.index(2))                         #output = 1
print(number.index(2,5))                        #output = 7
#8.extend():-
list1 = [1,4]
list2 = [6,8]
#list1.extend(list2)
#print(list1)                         #output = [1,4,6,8]
list2.extend(list1)
print(list2)                          #output =[6,8,1,4]
#.9 revese():-
item =[0,1,2,3,4,5,6]
item.reverse()
print(item)                            #output = [6,5,4,3,2,1,0]
#10.copy():-
a = [1,2,3,"seema","varsha"]
b = a.copy()
b.pop()
print(a)               #output =[1,2,3,"seema","varsha"]
print(b)                   #output = [1,2,3,"seema"]
#11.clear():-
a = [1,2,3,"seema","varsha"]
a.clear()
print(a)                           #output =[]



