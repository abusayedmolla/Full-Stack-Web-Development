def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

def modulus(x, y):
    return x % y

def main():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Exit")

        # Get user input for operation selection
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Exiting the program.")
            break

        if choice in ['1', '2', '3', '4', '5']:
            # Get user input for numbers
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            # Perform the chosen operation
            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                if result is None:
                    print("Error: Division by zero is not allowed.")
                    continue
                operation = '/'
            elif choice == '5':
                result = modulus(num1, num2)
                operation = '%'

            # Display the result
            print(f"{num1} {operation} {num2} = {result:.2f}")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

