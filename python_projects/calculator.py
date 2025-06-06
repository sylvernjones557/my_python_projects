def add(a,b):
    return int(a) + int(b)

def sub(a,b):
    return int(a) - int(b)

def pro(a,b):
    return int(a) * int(b)

def quo(a,b):
    return round((int(a) / int(b)) , 2)

goal = False
while not goal:
    num1 = input("Enter the first number\n")
    num2 = input("Enter the second number...\n")
    choice = input(
        "Enter your operation choice...\n + for addition\n - for subtraction\n * for multiplication \n and / for division\n")
    if choice == "+":
        result = add(num1, num2)
        print(f"the sum of {num1} and {num2} is :{result}")
    elif choice == "-":
        result = sub(num1, num2)
        print(f"the sum of {num1} and {num2} is :{result}")
    elif choice == "*":
        result = pro(num1, num2)
        print(f"the sum of {num1} and {num2} is :{result}")
    elif choice == "/":
        result = quo(num1, num2)
        print(f"the sum of {num1} and {num2} is :{result}")
    else:
        print("you entered the wrong option")
    option = input("Do you want use again.... \n press YES or press AGAIN to start from first or press NO to exit\n")
    if option.lower() == "yes":
        goal = False
    elif option.lower() == "no":
        goal = True

