"""Check whether a list contains duplicate values or not"""

# 1st Approach
lst = list(map(int, input("Enter the elements of the List: ").split()))
found = False
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            print(f"Duplicate value {lst[i]} found at positions {lst[i]} and {lst[j]}")
            found = True

if not found:
    print("No Duplicate Items Found...😁")


# 2nd Approach
lst = []
n = int(input("How many elements do you want in your List?"))
print("Enter the elements of the List: ")
for i in range(n):
    print(f"Enter {i+1} element:")
    lst.append(input())
print("Value of the List has been added successfully 👍")
print("Do you want to check whether your list contains Duplicate values or not?")
print("If Yes then Press 1.")
print("If No then Press 0.")
c = int(input("Enter your choice: "))
match c:
    case 0:
        print("Ok No Problem...😊")
    case 1:
        found = False
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    print(
                        f"Duplicate value {lst[i]} found at positions {i+1} and {j+1}"
                    )
                    found = True
        if not found:
            print("No Duplicate Items Found...😁")
    case _:
        print("Invalid Input...😵")
print(lst)