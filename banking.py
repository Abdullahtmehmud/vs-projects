import time
from datetime import datetime

# ATM Machine
# 1. Enter your pin
# 2. Menu/Options
# 3. Operations

balance = 0
history = []

def ask_again():
   print("Do you want to make any other transaction: ")
   choice = input("Yes/y or No/n: ")

   if choice.lower() == "y":
      time.sleep(2)
      interface_menu()

   elif choice.lower() == "n":
        print("Thank you for chosing us.")
   else:
      print("Invalid input")

def previous_transactions():
   print(history)

def cash_withdrawal():
   pass

def transfer_cash():
   pass

def cash_deposit(): 
   global balance
   amount = int(input("Enter the amount you want to deposit in your account: "))
   balance += amount
   date_time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
   history.append(f"{date_time} - Deposited{amount}, balance: {balance}")
   print(F"You've deposited amount: {amount}, Your new balance is: {balance}")
   
def balance_inquiry():
   global balance
   print("You're total balance is:", balance)

def exit():
    print("Do you want to end the transaction: ")
    choice = input("Yes(y)/No(n): ")
   
    if choice.lower() == "y":
     print("Thank you! Have a good day!")
    elif choice.lower() == "n":
        print("Continuing Transaction...")
        time.sleep(2.5)
        interface_menu()
    else:
      print("Invalid Input")     

def interface_menu():

    for i in range(1):
        print(
            "Select the options given: \n"
            " 1. Balance Inquiry \t 2. Previous queries \n"
            " 3. Cash Withdrawal \t 4. Cash Deposit \n"
            " 5. Transfer Cash \t 6. Exit"
        )

        choice = int(input("Enter your choice here: \n"))

        if choice == 1:
            time.sleep(2)
            balance_inquiry()

        elif choice == 2:
            time.sleep(2)
            pass

        elif choice == 3:
            time.sleep(2)
            pass

        elif choice == 4:
            time.sleep(2)
            cash_deposit()

        elif choice == 5:
            pass

        elif choice == 6:
            time.sleep(0.5)
            exit()
            
        else:
            print('Invalid Choice')
            break
        time.sleep(2.5)
        ask_again()

def startup():
    while True:
     
     pin = (input("Enter your pin: ".upper())).strip()

     if not pin.isdigit():   
      print("Add only keys please".upper())
      continue

     pin = int(pin)

     if pin == 0000:
         time.sleep(1)
         interface_menu()   
         break
     elif pin not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
           print("Invalid pin. please try again!".upper())

startup()