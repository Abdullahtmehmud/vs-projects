import math

# Making a Good Calculator with functions including:
# 1. Addition
# 2. Subtraction
# 3. Division
# 4. Multiplication
# 5. Modulus
# 6. Square root
# 7. Exponentiation

def exit():
    print("Thank you! Have a good day")

def ending():
     print("Invalid Choice")

def middle():
    print("You're doing great, Keep going!")

def calculator():
    print("Select any of the following (1-8) operator: ")
    print("1. Addition")
    print("2. Subtractiton")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Square root")
    print("7. Exponentiation")
    print("8. Exit")

    count = True
    count = 0
    first_time = True
    while True:
      if first_time:
          prompt = 'Chose: '
          first_time = False       
      else:
        prompt = 'Choose again: '

      count += 1
      if count == 3:
           middle()               
       
      try:
         num = int(input(prompt))
      except ValueError:
            print('Invalid Choice')
            continue                 
                
      if num == 8:
        exit()
        break
       
      elif num == 6:
                 x = float(input("Enter the number for square root: "))
                 if x < 0:
                    print("Cannot take square root for negative number")
                 else:
                    print('Result: ', math.sqrt(x))        
      
      elif num in [1, 2, 3, 4, 5, 7]:
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
                print("Result: ", x % y)   
      elif num == 7: 
                print('Result: ', x ** y)           
      else:
        if num not in [1, 2, 3, 4, 5, 6, 7, 8]:
          ending()  
           
calculator()