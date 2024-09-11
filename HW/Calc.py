def faulty_calculator():
    import random
    print("Welcome to the Faulty Calculator!")
    
    RNG1 = random()
    RNG2 = random()
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    if RNG1 == 45 and operator == '+' and RNG2 == 10:
        print(f"{num1} {operator} {num2} = 60 (Faulty Result)")
    elif RNG1 == 100 and operator == '-' and RNG2 == 20:
        print(f"{num1} {operator} {num2} = 50 (Faulty Result)")
    elif RNG1 == 9 and operator == '*' and RNG2 == 9:
        print(f"{num1} {operator} {num2} = 100 (Faulty Result)")
    elif RNG1 == 80 and operator == '/' and RNG2 == 8:
        print(f"{num1} {operator} {num2} = 15 (Faulty Result)")
        
    else:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                return
        else:
            print("Invalid operator! Please use +, -, *, or /.")
            return

        print(f"{num1} {operator} {num2} = {result}")