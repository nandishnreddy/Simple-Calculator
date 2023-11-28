def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


print("Choose from the following operations"
      "\n1.Addition"
      "\n2.Subtraction"
      "\n3.Multiplication"
      "\n4.Division")
select = int(input("Select the arthritic operation 1, 2, 3, 4"))
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
if select == 1:
    print(num1, "+", num2, "=", add(num1,num2))
elif select == 2:
    print(num1, "-", num2, "=", sub(num1,num2))
elif select == 3:
    print(num1, "*", num2, "=", mul(num1,num2))
elif select == 4:
    print(num1, "/", num2, "=", div(num1,num2))
else:
    print("Invalid Input")