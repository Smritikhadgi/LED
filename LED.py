#Create a function with variable length of arguments.
def myFun(*argv): 
    for arg in argv: 
        print (arg)
myFun('Hola', 'Welcome', 'to', 'SSIT')

#2. Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it.

# def outer(a,b):
#     x=a**2
#     def ine(a,b):
#         return a+b
#     add=ine(a,b)
#     return add+5
# result=outer(12,12)
# print(result)

# 3. Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name
#  show_tudent(name, age) to it and call it using the new name.

# def display_student(name,age):
#     print(name,age)
# display_student('pramesh',20)
# show_tudent=display_student
# show_tudent('pramesh',20)

# 4. Find the largest item from a given list.
# x=[1,2,3,4,5,6,7,8]\

# x=[1,2,3,4,5,6,7,8]
# print(max(x))

# 5. What is the difference between 10 / 3 and 10 // 3?

#10/3 implies division with integer number whereas 10//3 implies to representation of quotient of given operation(floor division)
# a=10
# b=3
# print(a/b)
# print(a//b)

# 6. What about two asterisks (**)?
# two asterisks represents the exponential value of give number
# a=2
# print(a**2)


# 7. What is the difference between local and global variables?

# local variable are the variables used when the operation is done within the
# local function, the local variable ends when the function ends.
# global variable are the variable used throughout the operation.

# 8. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.

# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return 'FizzBuzz'
#     if input % 3 == 0:
#         return 'Fizz'
#     if input % 5 == 0:
#         return 'Buzz'
#     return input
# print(fizz_buzz(33))
# print(fizz_buzz(5))

# 9. Write a function for checking the speed of drivers. 
# If speed is less than 70, it should print “Ok”.
# if the speed is 80, it should print: “Warning”.

# sp=int(input('enter the speed acquired by the driver; '))
# if sp<70:
#     print('Ok')
# else:
#     print('warning')

# 10. Write a program that prompts the user to input a positive integer.
#  It should then print the multiplication table of that number. 

# h=int(input('enter a postitve number; '))
# for a in range (1,11):
#     print(h,"x",a,'=',h*a)

# 11. Write a program that prompts the user to input an integer and then outputs the number with the digits reversed.
#  For example, if the input is 12345, the output should be 54321.

# s=int(input('enter a num; '))
# t=0
# while s>0:
#     c=s%10
#     t=t*10+c
#     s=s//10
# print('the rev of the number is', t)

# 12. Write a python program that return the number of characters in a string. 
# myList = "Parameter"

# p="CosmikDebries"
# q=0
# for i in range(0,(len(p))):
#     if p[i]!="":
#         q=q+1
# print('total characters on a string is:' +str(q))

# 13. Write a Python program to multiply all the numbers in a list using while and for loop.
# Sample list = [8,2,3,-1,7]

# def mul():
#     list=[8,2,3,-1,7]
#     ist=1
#     for i in range (0,5):
#         ist=list[i]+ist
#     print(ist)
# mul()

# 14. Write a Python program to sum all the numbers in a list using for loop and while loop.
# Sample list : [8, 2, 3, 0, 7]


# def add():
#     a=[8,2,3,0,7]
#     b=0
#     for i in range(0,5):
#         b=a[i]+b
#     print(b)
# add()

# 15. Accept string from the user and display only those characters which are 
# present at an even index

# def printEveIndexChar(str):
#       for i in range(0, len(str)-1, 2):
#         print("index[",i,"]", str[i] )
# inputStr = input("Enter String ")
# print("Orginal String is ", inputStr)
# print("Printing only even index chars")
# printEveIndexChar(inputStr)

# 16. Accept string from the user and display only those characters which are 
# present at an odd index.

# def char(str):
#     for i in range(1,len(str)-2,2):
#         print("index[",i,"]", str[i] )
# inputstr=input('enter a string; ')
# print('original string is', inputstr)
# print('printing only odd chars ')
# char(inputstr)
