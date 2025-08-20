# Making a to do list.
# 1. Add Task
# 2. View Task
# 3. Delete Task
# 4. Exit

tasks = []

def add_task():
    add = input('Enter a new task: ')
    tasks.append(add)
    print(f"Added: {add} ")
def view_task():
    global tasks
    for i, task in enumerate(tasks, 1):
     print(f"Your tasks are: \n{i}. {task}")
           
def delete_task():
    if tasks:
       print(f'Your tasks are: \n{tasks}')
       remove = input("Enter the task you want to remove: ")
    elif remove not in tasks:
       print('No such task added')
    elif remove in tasks:
       tasks.remove(remove)
       print(f'{remove} has been removed from tasks')   
      

while True:
     print("1.Add Task \t 2.View Task \n3.Delete Task  \t 4.Exit")
     choice = int(input("Chose any of the given: "))

     if choice == 1:
        add_task()
     elif choice == 2:
        view_task()
     elif choice == 3:
        delete_task()
     elif choice == 4:
        print("Thank you for chosing us!")
        break
     else:
        print("Invalid Choice. Chose the correct option")