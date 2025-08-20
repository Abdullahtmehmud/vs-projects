import time

# Making Shopping cart

cart = []
first_time = True

while True:
   if not first_time:
      time.sleep(1.5)
   else:
      bruh =False

   print("1.Add to cart \t 2.View cart \n3.Delete item \t 4.quit shopping")
   choice = input("Chose any option: ")
   item = ""   

   if choice == '1':
       item = input("Enter the item to add: ")
       cart.append(item)
       print(f'{item} has been added to your cart.')
   elif choice == '2':
         time.sleep(1)
         if cart:
            print("Your cart:")
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item}")
         else:
            print("Your cart is empty. add items to fill cart")
   elif choice == '3':
               
               
               item = input("select item to remove: ")
               cart.remove(item)
               print(f"{item} has been removed from your cart")
         
          print(f"no such {item} added before")
       
   else:
       print("Invalid option. Please chose the right option")

   