'''
what is python?
a python is high-level langauage, general-purpose programming language known for its simple, English-like syntax and high readability.

Key features:
• Readable syntax. Python uses indentation (spaces) to group blocks of code instead of curly brackets or semicolons, making programs look clean.
• Interpreted execution. Code runs line by line without needing a separate compilation step first, which speeds up testing and debugging.
• Cross-platform compatibility. Programs written on one operating system (Windows, macOS, or Linux) generally run on others without major changes.
• Massive ecosystem. Python includes a large built-in standard library alongside hundreds of thousands of free, third-party packages

Common Uses:
• Artificial intelligence and machine learning. Developers use frameworks like PyTorch and TensorFlow to train models and build AI agents.
• Data science and analysis. Libraries like Pandas, NumPy, and Matplotlib help analysts clean, calculate, and visualize large datasets.
• Web development. Frameworks such as Django and Flask power the back-end logic of websites and APIs.
• Task automation. Scripts can automate repetitive tasks like renaming files, organizing Excel spreadsheets, or scraping data from web pages.

types of mode

Shell mode (Interactive mode) runs code one command at a time with instant output, while Script mode runs a saved .py file all at once. Both use the exact same Python interpreter, just with different workflows.


1. Shell Mode (Interactive Mode)

Shell mode uses a REPL (Read-Eval-Print Loop). You type a line of code, press Enter, and Python immediately executes it and shows the result.
• How to start it: Open your computer's terminal or command prompt and type python (or python3). You will see the >>> prompt waiting for your input.

• Pros: Instant feedback; no need to create or save files; great for testing a single function or checking how a syntax rule behaves.
• Cons: Your code disappears as soon as you close the window; writing multi-line loops or long programs is awkward.


2. Script Mode

Script mode is the standard way developers build real programs. You write all your instructions in a text editor or IDE (like VS Code or PyCharm), save the file with a .py extension, and tell Python to execute the whole file from top to bottom.

• Pros: Code is saved permanently and can be edited, shared, or reused anytime; easily handles hundreds or thousands of lines of logic.
• Cons: You have to save the file and re-run it every time you make a change; expressions like 5 + 3 won't display on screen unless you explicitly wrap them in print().

'''

Name = "Prabanchan Arul"
print("My Name is :",Name)

'''
what is variable?
A variable in Python is a named container that stores a value in your computer's memory so you can use or change it later in your program

Examples:
name = "Priya"      # Stores text (string)
age = 22            # Stores a whole number (integer)
price = 99.50       # Stores a decimal number (float)
is_student = True   # Stores a True/False value (boolean)
'''

User_ID = 1126
Name = "prabanchan Arul"
print("User_id is :", User_ID)
print("Name is:", Name)

'''
example '''

Product = "Cricket Kit"
Price = 8000
Quantity = 15
Total = Price * Quantity
print(Product,Price,Quantity,Total)
print("product is:",Product)
print("price is:",Price)
print("Quantity is :",Quantity)
print("Total is:",Total)

'''
variable creation rules
1.start with letters or underscore ( example : Age,_age) 
2.cannot start with a number ( example : 2name is not allowed )
3.can contains letter,digits,underscores ( Example: Student_Name = )
4.cannot use python keywords as Variable Name

'''

'''Multiple values assigning '''
Name,Age,City = "prabanchan",21,"Cuddalore"
print(Name)
print(Age)
print(City)

'''
data types

1.int (numbers start from -ve to +ve numbers )
2.float ( point values examples : 9.00 )
3.boolean ( True or False )
4.string (characters)

'''

'''
Example
'''

Roll_No = 1126
Name = "Prabanchan Arul"
salary = 50000.00
is_working = True
print (type(Roll_No))
print("Employee Name is:", Name)
print("Employee salary is:",salary)
print("is Employee Working:",is_working)

A= 10
B= 20
C= A+B
print(A,B,C)
