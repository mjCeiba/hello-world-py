# This is a comment
# -*- coding: latin-1 -*-
'''
Helo this is a multi comment
'''

# Ask a user to input their name and assign it
# name = input('What is your name? ')
# print('Hello', name)

# listOfFruits = ["A", "B", "C", "D"]
# listOfFruits.append("E")
# listOfFruits[0] = "Z"
# del listOfFruits[0]
# print(listOfFruits)

## LIST

# list1 = [1, 2, 3, 4]
# list2 = [8, 7, 6, 5]
# max(list1)
# min(list2)

## DICTIONARIES
# students = {"BOB": 12, "Rachel": 13, "Emily": 28}
# students["BOB"] = 20
# print(students["BOB"])

# TUPLES
# tup = ('oranges', 'apples', 'banana')
# print(tup)


# Validation statements

# if 2 == 3:
#     print("TRUE")
# else:
#     print("FALSE")

# FOR LOOPS
# # list1 = ["Apples", "Bananas", "Cherries"]
# # tup = (18, 28, 23)
# #
# # for item in list1:
# #     print(item)
# #
# # for item in tup:
# #     print(item)
#
# # for item in range(-10, 10):
# #     print(item)
#
# # for i in range(0, 11, 2):
# #     print(i)
#
# for i in range(0, 5*5, 5):
#     print(i)


### WHILES AND CONTROL STATEMENTS
# c = 0
# while c < 5:
#     print(c)
#     c = c + 1
#

# while c < 5:
#     print(c)
#     if c == 3:
#         break
#     c = c + 1

# while c < 5:
#     c = c + 1
#     if c == 3:
#         continue
#     print(c)

# while c < 5:
#     if c == 3:
#         pass
#     print(c)
#     c = c + 1


### TRY and exceptions
# try:
#     if name > 3:
#         print("Hello")
# except:
#     print("Something wrong happend")

### FUNCTIONS

# def helloWorld():
#     print("Hello World")

# def greeting(name):
#     print("Hello " + name)

# greeting("Manuel")

# def sum(num1, num2):
#     return num1 + num2


## CLASSES
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sayName(self):
#         return "My name is " + self.name
#
#     def sayAge(self):
#         return "My age is " + str(self.age)
#
#
# person1 = Person("Julian", 41)
# print(person1.sayName())
# print(person1.sayAge())

### INHERINTANCE
# class Parent:
#     def __init__(self):
#         print("Parent class")
#
#     def parentFunc(self):
#         print("parent function")
#
#     def sayHi(self):
#         print("Hello")
#
#
# class Child(Parent):
#     def __init__(self):
#         print("this is child Class")
#
#     def childFunc(self):
#         print("This is child func")
#
#     def sayHi(self):
#         print("Child say hi")
#
#
# c = Child()
# c.sayHi()


calculationsToHours = 24
nameOfUnit = "hours"
_exit = True


def validateIsDigit(number_of_days):
    try:
        casted_number = int(number_of_days)
        if casted_number > 0:
            daysToUnits(int(casted_number))
        elif casted_number == 0:
            print("You entered 0, that's not a valid number")
    except ValueError:
        print("Apparently you're trying to break down my server, ¡DO NOT DO DAT!")


def daysToUnits(number_of_days):
    print(f"{number_of_days} days are {number_of_days * calculationsToHours} {nameOfUnit}")


while _exit:
    print("(if you want to finish the process type 'exit')")
    user_input = input("Hello please enter the number of days or a list separated by ',' : ")

    if user_input != 'exit':
        for number_of_days in user_input.split(","):
            validateIsDigit(number_of_days)
    else:
        print("Bye")
        _exit = False
