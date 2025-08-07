# Making a Good Calculator with functions including:
# 1. Addition
# 2. Subtraction
# 3. Division
# 4. Multiplication

def calculator():
        print("Select any of the following (1-4) operator: ")
        print("1. Addition")
        print("2. Subtractiton")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        first_time = True
        while True:
            if first_time:
                prompt = 'Chose: '
                first_time = False
            else:
                prompt = 'Choose again: '
            num = int(input(prompt))

            if num in [1, 2, 3, 4]:
                x = float(input("Enter your first number: "))
                y = float(input("Ener your second number: "))

                if num == 1: 
                 print('Result: ', x + y)    
                elif num == 2:
                    print('Result: ', x - y)
                elif num == 3:
                    print('Result: ', x * y)
                elif num == 4:
                    if y == 0:
                        print("Cannot be divided by zero")   
                    else:
                        print('Result: ', x / y)   
            elif num == 5:
                    print('Thank you! Have a good day!')
                    break
            else:
                 print('invalid choice')

calculator()
