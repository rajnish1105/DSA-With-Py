def ExceptHandling(a, b):
    print("This is the Exception Handling Program")
    x = input("What You want to do ?\n +, -, *, /  : ")
    match x:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            try:
                r = a/b
            except ZeroDivisionError:
                print("Cannot be Divided by Zero")
        case _:
            print("Invalid Input")

a = int(input("Enter the First Number : "))
b = int(input("Enter teh Second Numebr : "))       
ExceptHandling(a, b) 