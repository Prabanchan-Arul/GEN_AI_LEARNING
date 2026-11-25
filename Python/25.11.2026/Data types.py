# integer
a= 10
b= -45
print(a,b)

# FLoat
c= 87.33
d= -222.34
print(c,d)

# string
str1 = 'single string example'
str2 = "double string example"
str3 = '''triple string example'''
print(str1,str2,str3)

# boolean
is_active = True
is_member = False
print(is_active,is_member)

# list
cart = [1,"Mobile",56000,2,"laptop",78000,4.7]
print(cart)

# tuple
details = (1,"hdfc","hdfc245", True)
print(details)

# Set
set_eg = {1,2,3,4,4,5,6,6,7,8,9,9,10}
print(set_eg)

# dictionary
dict_1 = {"User_id": 1, "Name":"Prabanchan Arul"}
print(dict_1)

# None
Total = None
print(Total)

# type Convertion
# implicit Type Convertion
'''
Implicit conversion (also known as type coercion) is the automatic conversion of one data type into another by a compiler, interpreter, or database engine without requiring explicit instructions from the programmer.'''

# Example 1
a = 10
b = 2.5
Result = a+b
print(type(Result))

# Example 2
num_1 = 15
num_2 = 5
result = num_1/num_2
print(type(result))

# Example 3
num_3 = 10
num_4 = 5
result = num_3 + num_4
print(type(result))

# exapmle 4
num_3 = 10
num_4 = 5
result = num_3 - num_4
print(type(result))

# Example 5
num_3 = 10
num_4 = 5
result = num_3 % num_4
print(type(result))

# Explicit
''' Explicit type conversion (also called type casting) is the manual conversion of an object from one data type to another using Python's built-in functions.'''

# example 1
num_1 = int(25.0)
print(num_1)
print(type(num_1))
num_2 = float(25)
print(num_2)
print(type(num_2))

num_3 = int("34")
print(num_3)
print(type(num_3)) # number can change from str to int but characters cannot be changed

# input Function and output function
Name = input("Enter Your Name :")
print("name is :",Name)

Marks = int(input("Enter Your Marks:"))
print("Marks is:",Marks)


Student_name = input("enter your name:")
total_marks = int(input("Enter your marks:"))
Average_mark = float(input("enter your average:"))
Course = input("which Course you want to choose:")
is_willing = bool(input("are you willing to go abroad for studies:"))

print("Student Name is:",Student_name)
print("the total marks is :",total_marks)
print("the average mark of the student is:",Average_mark)
print("the course chosen by student is:",Course)
print("willing to go abroad for studies:",is_willing)


a,b = input("Enter you numbers:").split()
print(int(a)+int(b))

# add the two number
Num_1,Num_2 = input("enter you numbers:").split()
print(int(Num_1) + int(Num_2))

# Swapping
a = 10
b = 20
a,b = b,a
print("After swap:",a,b)

# using Temp
a = 100
b = 200
temp = 0
temp = a
a = b
b = temp
print("after swapping:",a,b)

# to check positive integer
user_input = int(input("Enter your Number:"))

if user_input > 0:
    print("the Number is positive")
else:
    print("the number is negative")

Num_1 = int(input("Enter your number1:"))
Num_2 = int(input("Enter your number2:"))

result = Num_1 - Num_2
print(result)

# To find Area of Circle
r = int(input("Enter the Radius:"))
pi = 3.14
area = pi * r * r
print("radius of Circle is :",r)
print("the value of pi:",pi)
print("the area of the circle is :",area)

# repeat the string
str_1 = input("enter string1:")
str_2 = input("enter string2:")
print("the first string is:",str_1)
print("the seconf string is:",str_2)
print(str_1*2,str_2*3)
