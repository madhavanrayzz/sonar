# main.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("Welcome to Simple Calculator!")
    print("Type 'q' to quit\n")

    while True:
        try:
            num1_input = input("Enter first number: ").strip()
            if num1_input.lower() in ['q', 'quit']:
                print("Goodbye!")
                break

            num1 = float(num1_input)

            num2_input = input("Enter second number: ").strip()
            if num2_input.lower() in ['q', 'quit']:
                print("Goodbye!")
                break

            num2 = float(num2_input)

            op = input("Enter operation (+ - * /): ").strip()

            if op in ['q', 'quit']:
                print("Goodbye!")
                break

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation!")
                continue

            print(result)

        except ValueError:
            print("Invalid number input!")
        except Exception as e:
            print("Something went wrong!")
