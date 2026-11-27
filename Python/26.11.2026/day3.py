# operators
# definition:
'''
operators are special symbols or keywords used to perform computations and logical operations on variables and values '''

# types of operators

Arithmetic operator ( +,-,*,/,//,%,**)
comparison operator ( ==,<=,>=,<,>,!=)
assignment operator (=, +=,-=,*=,/=,//=,%=,**=)
logical operator (and,or,not)
membership operator (in,not in)
identity operator ( is ,is not)
bitwise operator (& | ^ ~ << >>)

#example for arithmetic operator
num_1=int(input("enter your number1:"))
num_2=int(input("enter your number2:"))

value_of_addition = num_1 + num_2
print("the addition value is :",value_of_addition)

value_of_subtraction = num_1 - num_2
print("the subtracted value is:",value_of_subtraction)

value_of_multiplication = num_1 * num_2
print("the multiplied value is :",value_of_multiplication)

value_of_division = num_1/num_2
print("the divided value is:",value_of_division)

value_of_floordivision =num_1//num_2
print("the floor divide values is:",value_of_floordivision)

value_of_mod_division = num_1 % num_2
print("the mod divided value is:",value_of_mod_division)

value_of_expo = num_1 ** num_2
print("the expo value is:",value_of_expo)

# example for comparison operator
num1=int(input("enter your number1:"))
num2=int(input("enter your number2:"))

print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)


# using in string

user_input = input("enter your username:")
password = input("enter your password:")
if (user_input == "test" and password == "test@123"):
    print("login successful")
else:
    print("check your credentials")

# or operator example

Age = int(input("enter your age:"))
Voter_ID = bool(input("enter your status:"))
if (Age >=18 or Voter_ID == True):
    print("eligible for voting")
else:
    print("not eligible for voting")


# example 2 for OR operator
# -> if using bool to get input it will consider no input has 0(false) it has value it will consider as 1(true)
amount = int(input("Enter amount:"))
Coupon = bool(input("enter True or False:"))
if (amount >= 5000 and Coupon == True):
    discount = 0.05*amount
    total_amount = amount-discount
    print("the total amount after discount is :",total_amount)
elif (amount >= 4000 and Coupon == True):
    discount = 0.04*amount
    total_amount = amount-discount
    print("the total amount after discount is :",total_amount)
elif (amount >= 3000 and Coupon == True):
    discount = 0.03*amount
    total_amount = amount-discount
    print("the total amount after discount is :",total_amount)
else:
    print("no discounts")


# example

a = int(input("enter number1:"))
b = int(input("enter number2:"))
c = int(input("enter number3:"))

if(a>=b and a>=c):
    print("A is greater")
elif(b>a and b>c):
    print("B is greater")
else:
    print("C is greater")

# Assignment operator
acc_bal = 10000
acc_bal += 200
print("total:",acc_bal)

# membership operator
cart = ["mobile","laptop","bat","Tablet"]
print("mobile" in cart)
print("bat" not in cart)

# identity operator
a = 10
b = 25
c = b
print( a is b)
print( c is b)

# bitwise operator
print(bin(8))
print(bin(8>>1))
