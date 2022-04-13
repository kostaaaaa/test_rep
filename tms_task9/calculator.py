class Calculator:
    @staticmethod
    def add(x, y: float) -> float:
        return x + y

    @staticmethod
    def subtract(x, y: float) -> float:
        return x - y

    @staticmethod
    def multiply(x, y: float) -> float:
        return x * y

    @staticmethod
    def divide(x, y: float) -> float:
        return x / y

    @staticmethod
    def menu():
        print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n0.EXIT!")
    
    @staticmethod
    def ask_nubers():
        num1 = float(input("Enter first number: ")) 
        num2 = float(input("Enter second number: "))
        return num1, num2
    
    @classmethod
    def main(cls):
        while True:
            try:
                Calculator.menu()
                choice = input("Enter choice: ")

                if choice in ('1', '2', '3', '4', '0'):
                    if choice == '1':
                        num1, num2 = cls.ask_nubers()
                        print("Result: ", cls.add(num1, num2))

                    elif choice == '2':
                        num1, num2 = cls.ask_nubers()
                        print("Result: ", cls.subtract(num1, num2))

                    elif choice == '3':
                        num1, num2 = cls.ask_nubers()
                        print("Result: ", cls.multiply(num1, num2))

                    elif choice == '4':
                        num1, num2 = cls.ask_nubers()
                        print("Result: ", cls.divide(num1, num2))
                    elif choice == '0':
                        print('See you later!')
                        return
                else:
                    print('\nInvalid input! Try again ;)\n')
            except ZeroDivisionError:
                print('\nAre you feeling good?\n')
                continue
            except ValueError:
                print('\nEnter numbers please!\n')    
                continue

Calculator.main()