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
dict = {
    "name": "Aman hussain",
    "class": "2nd year",
    "group": "Pre-engineering",
    "Subject": {
        "urdu": 57,
        "English": 65,
        "PST": 38,
        "Mathematic": 72,
        "physics": 54,
        "chemistry": 47,
    }
}
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
collection  = set()
collection.add(1)
collection.add("aman")
collection.add(2)

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