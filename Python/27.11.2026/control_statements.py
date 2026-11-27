#1. Conditional Statements
#1a.simple if
num = -2
if num >=0:
    print("postive number")
else:
    print("negative number")

#1b.multiple condition
user_input = input("enter a whether type(cloudy/sunny):")

if (user_input == "cloudy"):
    print("go to movie")
elif (user_input == "sunny"):
    print("go to beach")
else:
    print("stay at home")

#1c.nested if statements
#example
user_pin = int(input("enter a pin:"))
acc_balance = 50000
withdraw_money = int(input("enter a amount to withdraw:"))
balance = 0
if (user_pin == 2026):
    if(withdraw_money < acc_balance):
        print("acmount can be withdrawn")
        balance = acc_balance - withdraw_money
        print("balance money",balance)
    elif(withdraw_money == acc_balance):
        print("cannot be withdrawn")
    else:
        print("insufficient funds")
else:
    print("invalid pin")

#2.looping condition
#2a. For loop
list1 =[10,"praba",9.0,"laptop"]
for i in list1:
    print(i,end=" ")
#2b. for loop with else
list1 =[10,"praba",9.0,"laptop"]
for i in list1:
    print(i,end=" ")
else:
    print("loop completed")


#2c. while loop
i = 0
while (i<=10):
    print(i,end=" ")
    i+=1 # i = i+1
   

# break
for i in range(2,51,2):
    if i == 30:
        break
    print(i,end=" ")
   
# continue
for i in range(2,51,2):
    if i == 32:
        continue
    print(i,end=" ")

# example
pin = 2026
attempt = 0

while( attempt<=3):
    user_pin = int(input("enter a pin:"))
    if user_pin == pin:
        print("correct pin")
        break
    else:
        print("wrong pin")
    attempt+=1
if attempt > 3:
    print("account blocked")


# pattern printing
for i in range(1,7):
    for j in range(i):
        print("*",end = " ")
    print()
    
# inverted traingle printing
for i in range(7,1,-1):
    for j in range(i):
        print("*",end = " ")
    print()
