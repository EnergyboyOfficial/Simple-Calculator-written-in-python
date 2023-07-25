def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_symmetric(num):
    return str(num) == str(num)[::-1]

def double_digits_sum_10():
    return [x for x in range(10, 100) if sum(map(int, str(x))) == 10]

def print_menu():
    print("Pip-Calc V4")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Check Prime")
    print("6. Check Whether the Number is Symmetric")
    print("7. Print all Double Digits Numbers whose Sum of Digits is Equal to 10")

print_menu()

while True:
    choice = input("Enter operation number (or 'q' to quit): ")

    if choice.lower() == 'q':
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please enter a valid operation number.")
    elif choice == '5':
        num = int(input("Enter a number to check if it's prime: "))
        if is_prime(num):
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
    elif choice == '6':
        num = int(input("Enter a number to check if it's symmetric: "))
        if is_symmetric(num):
            print(num, "is symmetric.")
        else:
            print(num, "is not symmetric.")
    elif choice == '7':
        double_digits = double_digits_sum_10()
        print("Double digits numbers whose sum of digits is equal to 10:", double_digits)
    else:
        print("Invalid choice. Please enter a valid operation number.")
