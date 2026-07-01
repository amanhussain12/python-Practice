#  print
# print("hello world")

# input
# name = input("My name is :")
# print(name)

# data type
   # int
# name = int(input("what is your age :"))
# print(f"i am {name} year old")

    #  float 
# a = 10.5
# total = float(input("your number :"))
# print(a + total )

# operators
# arthmetic operator + - * / % **
# a = 20
# b = 30
# answer = a * b
# answer = a + b
# answer = a - b
# answer = a / b
# answer = a % b
# answer = a ** b
# print(answer)

# string function

# str1 = "i am learning  in python"
# str2 = "hello"
# print(str1+str2)

# str = "i am a coder"
# print(str.endswith["er"])

# length string function 
# str1 = input("i am learning  in python :")
# print("lenght of your name is", len(str1))

# count function string 
# str = "i am learning  in python"
# print(str.count("a"))

# endwith
# str1 = "i am learning  in python"
# print(str1.endswith("thon"))

# capitalize
# str1 = "i am learning  in python"
# print(str1.capitalize())

# find
# str1 = "i am learning  in python"
# print(str1.find("in"))

# replace
# str1 = "i am learning  in python"
# print(str1.replace("python" , "javascript"))

# negative slicing index
# str1 = "i am learning in python"
# print(str1[-19 : -10]) 

# slicing string
# str1 = "i am learning  in python"
# print(str1[ 2 : 14])

# Conditional Statements
    # if , elif , else
# marks = int(input("enter your marks : "))

# if(marks >= 90):
#     grade = "A1"

# elif(marks >= 80 and marks < 90):
#     grade = "A"
# elif(marks >= 70 and marks < 80):
#     grade = "B"
# elif(marks >= 60 and marks < 70):
#     grade = "C"
# elif(marks >= 50 and marks < 60):
#     grade = "D"
# else:
#     grade = "Fail"

# print("your grade is :", grade)    

# nesting 
# age = 79

# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     pri(nt("cannot drive")

#  Practice Questions

# num = int(input("enter your number :"))

# if(num % 2 == 0):
#     print("EVEN NUMBER")
# else:
#     print("ODD NUMBER")

# a = int(input("enter first number :"))
# b = int(input("enter second number :"))
# c = int(input("enter third number :"))

# if(a >= b and a >= c):
#     print("first num is largest num ", a)
# elif(b >= c):
#     print("second num is largest num ", b)
# else:
#     print("third num is largest num" , c)

# num = int(input("enter number :"))

# if(num % 7 == 0):
#     print("multiple in 7")
# else:
#     print("cannot multiple")

# list in python
# marks = [20 ,30 ,40 ,50 ,60]
# print(marks)

# list slicing
# marks = [ 30 , 40 , 50 , 60 , 70 ]
# print(marks[1 : 3])
# print(marks[-3 : -1])

# list methods
    # append add one element at the end
# list = [ 20 ,30 ,40 ,50 ,60 ]
# list.append(70)
# print(list)

    # sort in ascending  order
# list = [ 60 , 50 , 40 , 30 , 20]
# list.sort()
# print(list)

    # sort reverse (sort in descenting order)
# list = [ 60 , 50 , 40 , 30 , 20]
# list.sort(reverse=True)
# print(list)

    # reverse list
# list = ['a' , 'b' , 'c' , 'd' , 'e']
# list.reverse()
# print(list)

    # insert element at index
# list = [ 1 , 2 , 4 ,5 ]
# list.insert(2 , 3)
# print(list)

    # removes first occurrence of element 
# list = [ 0 , 1 , 1 , 2 , 3 ]
# list.remove(1)  # ye dekhe ga ke phla 1 konsa hai is ko remove kr dega
# print(list)

    #  pop remove element at index
# list = [ 0 , 1 , 2 , 2 , 3 , 4 ]
# list.pop(3)
# print(list)

# Tuple 
# list = ( 1,)
# print(list)
# print(type(list))

# tuple method 
    # tup.index(element) return index of first occurrence
# tup = ( 1, 2, 3, 4, 5,)
# print(tup.index(4))

    # tuple.count
# tup = (1, 2, 3, 4, 5, 2, 2,)
# print(tup.count(2))

# practice Question 
# movies = []

# mov1 = str(input("enter first movie name :"))
# mov2 = str(input("enter second movie name :"))
# mov3 = str(input("enter third movie name :"))

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# list1 = input("enter a palindrome word : ")

# my_list = list(list1)

# copy_list = my_list.copy()
# copy_list.reverse()

# if(my_list ==  copy_list):
#     print("Palindrome")
# else:
#     print( "Not Palindrome")

# grade = input(" Enter a grade : ")

# tup = ( "C" , "B" , "A" , "A" , "C" , "A" , "B" , "D" ,"C")
 
# count =  tup.count(grade)

# print(count)

# List = ["C" , "B" , "A" , "A" , "C" , "A" , "B" , "D" ,"C"]
# List.sort()
# print(List)

# fruit = []
# fruit.append(input("Enter Your 1st Fruit Name : "))
# fruit.append(input("Enter Your 2nd Fruit Name : "))
# fruit.append(input("Enter Your 3rd Fruit Name : "))
# fruit.append(input("Enter Your 4th Fruit Name : "))
# fruit.append(input("Enter Your 5th Fruit Name : "))

# print(fruit)

# word = input("Enter Your Word : ")

# word2 = []
 
# count = word2.count(word)

# print(count)

        # dictionary
# dictionary are used to store data value in key:value pairs
# they are unordered , mutable(changeable) & don't allow duplicate key

# dict = {
#     "name" : "aman",
#     "age" : 20,
#     "goals" : ("software engineer" , "programmer"),
#     "dream" : ["pilot" , "enterprinior"],
#     "is_adult" : True,
#     12.99 : 94.4
# }

# dict["name"] = "Aman"
# dict["surname"] = "Hussain"
# print(dict)

        # nested dictionary
# dict = {
#     "name": "Aman hussain",
#     "class": "2nd year",
#     "group": "Pre-engineering",
#     "Subject": {
#         "urdu": 57,
#         "English": 65,
#         "PST": 38,
#         "Mathematic": 72,
#         "physics": 54,
#         "chemistry": 47,
#     }
# }
# print(dict["Subject"])
# print(dict)

        # dictionary methods
    # myDict.keys()  #returns all keys
# dict = {
#     "name": "Aman hussain",
#     "class": "2nd year",
#     "group": "Pre-engineering",
#     "Subject": {
#         "urdu": 57,
#         "English": 65,
#         "PST": 38,
#         "Mathematic": 72,
#         "physics": 54,
#         "chemistry": 47,
#     }
# }
# print(dict.keys())
# print(list(dict.keys()))
# print(len(list(dict.keys())))

    # myDict.value() #returns all values
# print(dict.values())
# print(list(dict.values()))
# print(len(list(dict.values())))

    # myDict.items() #returns all (keys,values) pairs as tuples
# print(dict.items())
# print(list(dict.items()))
# print(len(list(dict.items())))

    # myDict.get("key") #returns the key according to value 
# print(dict["name1"]) # error
# print(dict.get("name1")) # none

    # myDict.update(newDict) # inserts the  specified  items  to the  dictionary 
# new_dict = {"section": "B" , "college name":"Pechs college"}
# dict.update(new_dict)
# print(dict)  

        
    # set in python 
# set is the collection  of the unordered items
# each element  in the set must be  unique  &  immutable

# collection = { 1, 2, 3, 4, "hello", "aman" , 1, 2, 3, 4, 5, }
# print(collection)

# collection = set()  # empty set 
# print(type(collection))

    #  set methods
# set.add()  # add an element
# collection  = set()
# collection.add(1)
# collection.add("aman")
# collection.add(2)

# print(collection)

# set.remove() # remove the element

# collection.remove(2)
# collection.remove("aman")
# print(collection)

# set.clear() # empties the set

# collection.clear()
# print(collection)

# set.pop() # remove the the random value

# collection.pop()
# print(collection)

# sets = {"aman" , "hussain" , "hello"}
# print(sets.pop())

#  set.union(set2) # combine both side values & returns new

# set1 = {1, 2, 3, 5 , 7 , 0}
# set2 = {4, 0, 6, 7 , 8 , 9}

# print(set1.union(set2))

#  set.intersection(set2) # combine common values & returns new 

# print(set1.intersection(set2))

    # Practice Question

#  Q1 dict = {
#     "cat" : "a small animal",
#     "table" : ["this is a facgniture table" , "list of facts & figures"]
# }

# print(dict)

# Q2
# set1 = {"python","java","c","python","javascript"}
# set2 = {"java","python","javascript","c","c"}

# print(len(set1.union(set2)))

# Q3

# marks = {}

# x = int(input("enter phy marks : "))
# marks.update({"phy" : x})

# x = int(input("enter chem marks : "))
# marks.update({"chem" : x})

# x = int(input("enter math marks : "))
# marks.update({"math" : x})

# x = int(input("enter english marks : "))
# marks.update({"enlish" : x})

# x = int(input("enter urdu marks : "))
# marks.update({"urdu" : x})

# x = int(input("enter islamiat marks : "))
# marks.update({"islamiat" : x})

# print(marks)

        # loops in python
# loops are used to repeat instructions
#  loops 2 hoty hain 1) while loops 2) for loops

# i = 1
# while i <= 10000:
#     print("Aman" , i)
#     i += 1
#  print(i)

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# Q1
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# Q2
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# Q3
# n = 3
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

# Q4
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

# Q5
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100 , 25]
# x = int(input("Enter the num :"))
# i = 0
# while i < len(list):
#     if list[i] == x:
#         print("found at index", i)
#     else:
#         print("finding..." , i)
#     i += 1

# i = 1
# while i <= 10:
#     print(i)
#     if (i == 3):
#         break #used to ter,imate the loop when encountered
#     i += 1 

# i = 0
# while i <= 10:
#     if (i == 3):
#         i += 1 
#         continue #used to ter,imate the loop when encountered
#     print(i)
#     i += 1

# i = 0
# while i <= 100:
#     if (i%6 == 0):
#         i += 1 
#         continue #used to ter,imate the loop when encountered
#     print(i)
#     i += 1

# for loops
# num = [1, 2, 3, 4, 5]
# for val in num:
#     print(val)

# str = "Aman Hussain"

# for char in str:
#     if (char == "a"):
#         print("found")
#         continue
#     else:
#         print("end")


# for num in list:
#     print(num)
    
# list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25)
# x = int(input("Enter a Num...:"))

# idx = 0
# for el in list:
#     if (el == x):
#         print("idx", idx);

#     idx += 1

# range()
# range function returns a sequence of number, starting from 0 by defualt, and icrements by 1 
# (by defualts), and stops before specified number.

# seq = range(5)

# for i in seq:
#     print(i)

# for i in range(10): # stop value
#     print(i)    

# for i in range(2, 10): # starting & stoping value
#     print(i)    

# for i in range(2, 101, 2): # start , stop & step value
#     print(i)    

# Q1
# for i in range(1, 101):
#     print(i)


# Q2
# for i in range(100 , 0 , -1):
#     print(i)

# Q3

# n = int(input("Enter the num... :"))

# for i in range(1 , 11):
#     print(n * i)

# n = int(input("enter the sum number :"))

# sum = 0 
# for i in range(1, n+1):
#     print(i)
#     sum += i

# print("total sum", sum)

# i = 1
# while i <= n:
#     print(i)
#     sum += i
#     i += 1

# print("total sum ", sum)

# n = int(input("enter a factorial number "))
# fact = 1
# i = 1

# while i <= n:
#     print(i)
#     fact *= i
#     i += 1

# print("factorial value", fact)

# n = 5
# fact = 1

# for i in range(1 , n+1):
#     fact *= i

# print("factorial =", fact)

#               function Defination
# def calc_add(a, b, c): # parameter
#     sum = a + b + c
#     add = sum * 3
#     print(add)
#     return add

# calc_add(5, 18, 24) # arrgument

#           Function 2 types
# Buit-in function         |  # user defined function
    # print() # len()      |  
    # type()  # range()    |    jo user khud banata hai function    

# defult parameter

# def calc_num(a=3 , b=9):
#     print(a*b)
#     return

# calc_num()

# practice questions

# Q1
# num = [ 1, 2, 3, 4, 5]

# def calc_list(list):
#     print(len(list))

# calc_list(num)

# Q2
# cities = ["karachi", "lahore", "islamabad"]
# cities1 = ["peshawar", "multan", "quetta"]

# def print_cities(list):
#     for item in list:
#       print(item, end=" ")

# print_cities(cities)
# print_cities(cities1)

# Q3

# n = 5
# fact = 1
# i = 1

# def find_fact(fact):
#     for i in range(1 , n+1):
#         fact *= i
#         print("factorial =", fact)

# find_fact(fact)

# n = int(input("enter a factorial number "))

# def find_fact(n):
#     fact = 1
#     i = 1
#     while i <= n:
#         fact *= i
#         i += 1
#         print("factorial value", fact)

# find_fact(8)

# price = int(input("How much Dollar in PKR :"))

# def converter(usd_val):
#     pkr_val = usd_val * 279
#     print(usd_val , "USD =" , pkr_val , "PKR" )

# converter(price)

#  home work problem solving

# num = int(input("Enter a Num : "))

# def explain(num):
#     if(num % 2 == 0 ):
#         print("EVEN NUMBER")
#     else:
#         print("ODD NUMBER")

# explain(num)    


    #  Recursion
# when a functions calls itself repeatedly

# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)

# show(5) 

# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return fact(n-1) * n

# print(fact(7))

# def cal_sum(n):
#     if n == 0:
#         return 0
#     return cal_sum(n-1) + n

# sum = cal_sum(50)
# print(sum)

# def cal_sum(n):
#     if n == 1 or n == 0:
#         return 0
#     return cal_sum(n-1) - n

# sum = cal_sum(5)
# print(sum)


def cal_list(list , idx=0):
    if idx == len(list):
        return
    print(list[idx])
    cal_list(list, idx+1)

family = ["aman", "abad", "manahil", "mehwish", "rizwan", "pervaz"]
cal_list(family)