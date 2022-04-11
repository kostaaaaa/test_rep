class Calculator:
    def add(x, y: float) -> float:
        return x + y

    def subtract(x, y: float) -> float:
        return x - y

    def multiply(x, y: float) -> float:
        return x * y

    def divide(x, y: float) -> float:
        return x / y


    print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

    while True:
        try:
            choice = input("Enter choice: ")

            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result: ", add(num1, num2))

                elif choice == '2':
                    print("Result: ", subtract(num1, num2))

                elif choice == '3':
                    print("Result: ", multiply(num1, num2))

                elif choice == '4':
                    print("Result: ", divide(num1, num2))
            else:
                print('\nInvalid input! Try again ;)\n')
        except ZeroDivisionError:
            print('\nAre you feeling good?\n')
            continue
        except ValueError:
            print('\nEnter numbers please!\n')    
            continue