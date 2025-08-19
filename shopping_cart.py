import time

# Making Shopping cart

cart = []
bruh = True

while True:
   if not bruh:
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
         if cart:
            print("Your cart:")
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item}")
         else:
            print("Your cart is empty.")
   elif choice == '3':
       print(cart)
       item = input("select item to remove: ")
       cart.remove(item)
       print(f"{item} has been removed from your cart")
   else:
      print("no such item added before")
      
   if choice == '4':
      print('Thank you for shopping with us!')
      break
   else:
    print("Invalid choice. please chose again")
    