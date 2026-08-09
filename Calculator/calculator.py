def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Choose between 1, 2, 3, 4, 5")

for i in range(1, 100):
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    option = int(input("Enter your option: "))

    if option == 5:
        print("Exiting...")
        break

    elif option in [1, 2, 3, 4]:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if option == 1:
            print(num1, "+", num2, "=", add(num1, num2))

        elif option == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif option == 3:
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif option == 4:
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid option!")