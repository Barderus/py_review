def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        print("You cannot divide by 0.")
        return None
    return a / b


def multiply(a, b):
    return a * b


def main():
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        choice = input("Enter your choice (1-4): ")

        if choice not in {'1', '2', '3', '4'}:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = divide(num1, num2)
            if result is not None:
                print(f"{num1} / {num2} = {result}")
        elif choice == '4':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")

        keep_going = input("Would you like to continue (Y/N)? ").upper()
        if keep_going == 'N':
            print("Exiting the calculator. Goodbye!")
            break


if __name__ == '__main__':
    main()
