num1 = float(input("Enter number 1: "))
operation = input("Choice operator +, -, / or *")
num2 = float(input("Enter number 2: "))
try:

    if operation =="+":
        result = num1+num2
    elif operation == "-":
        result = num1-num2
    elif operation == "*":
        result = num1*num2
    elif operation == "/":
        if num2 != 0:
            result =num1/num2
    else:
        print("Nelzya delit na zero")
except ValueError or NameError:
    print("Error")

print(num1, operation, num2, "=", result)