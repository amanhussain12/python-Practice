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

word = input("Enter Your Word : ")

word2 = []
 
count = word2.count(word)

print(count)