# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function to interact with the user
def main():
    print("Simple Calculator")
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'exit' to end the program")

        user_input = input(": ")

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input in ["add", "subtract", "multiply", "divide"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("Result:", add(num1, num2))
            elif user_input == "subtract":
                print("Result:", subtract(num1, num2))
            elif user_input == "multiply":
                print("Result:", multiply(num1, num2))
            elif user_input == "divide":
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print("Result:", result)
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please enter a valid operation.")
# Executing the program's main() function
if __name__ == "__main__":
    main()
