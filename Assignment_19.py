# 1. Write a python program to create a simple function which prints “Nikhil Verma”.
def printing():
    print("Nikhil Verma")


printing()


# 2. Write a python program to create a function which expects two arguments and print them in the function body.
def twoArgs(a, b):
    print(f"The 1st Argument is : {a}")
    print(f"The 2nd Argument is : {b}")


m = input("Enter the 1st Argument : ")
n = input("Enter the 2nd Argument : ")
twoArgs(m, n)


# 3. Write a python program to create a function which expects an unknown number of arguments.
def UnknownNumebrofArgs(*num):
    for i in num:
        print(i)


UnknownNumebrofArgs(10, 20, 50, 80, 90)


# 4. Write a python program to create a function which expects kwargs arguments.
def kwargsArgument(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


n = int(input("Enter the total number of arguments : "))
data = {}
for i in range(n):
    key = input("Enter key : ")
    value = input("Enter value : ")
    data[key] = value
kwargsArgument(**data)


# 5. Write a python program to create a function which expects a list as an argument.
def listArg(l):
    print(f"List is : {l}")


lst = [1, 5, 9, 8, 3, 7, 6]
listArg(lst)


# 6. Write a python program to create a function that finds a maximum of four numbers
def maxNum():
    a = int(input("Enter the 1st Number : "))
    b = int(input("Enter the 2nd Number : "))
    c = int(input("Enter the 3rd Number : "))
    d = int(input("Enter the 4th Number : "))
    max_value = max(a, b, c, d)
    print(max_value)


maxNum()


# 7. Write a python program to sum all the numbers in a list.
def sumAll(l):
    total = 0
    for i in l:
        total += i
    print(total)


lst = [5, 8, 6, 7, 3, 2]
sumAll(lst)


# 8. Write a python program to multiply all the numbers in a list.
def product(l):
    pro = 1
    for i in l:
        pro *= i
    print(pro)


lst = [2, 7, 3, 5, 4]
product(lst)


# 9. Write a python program to create a function to check whether a number falls in a given range.
def checkExistence(m, n):
    i = int(input("Entetr the target value : "))
    if i in range(m, n + 1):
        print("The Value Exists between the range")
    else:
        print("The Value does not Exist between the range")


a = int(input("Enter the Starting value of the range : "))
b = int(input("Enter the Ending value of the range : "))
checkExistence(a, b)


# 10. Write a python program to create a function to check whether a given number is even or odd.
def EvenOdd(a):
    if a % 2 == 0:
        print(f"{a} is Even")
    else:
        print(f"{a} is Odd")


n = int(input("Enter the Numebr : "))
EvenOdd(n)