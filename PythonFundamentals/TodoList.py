todo_list = []

def ask_option():
    print("========================")
    print("1 . add task")
    print("2 . remove task")
    print("3 . list tasks")
    print("4 . end program")
    print("========================")


def list_tasks():
    if len(todo_list)==0:
        print("There are no tasks")
    else:
        for i , task in enumerate(todo_list,1):
            print(f"{i} . {task}")


def add_task():
    task = input("Enter your task: ")
    todo_list.append(task)
    print(f"{task} is added")


def remove_task():
    if len(todo_list) == 0 :
        print("There are no tasks")
        return

    try:
        list_tasks()
        to_delete = int(input("Enter task number to remove: "))
        if 1 <= to_delete <= len(todo_list):
            todo_list.pop(to_delete - 1)
            print(f"task number {to_delete} is removed")
        else:
            print("invalid task number")
    except ValueError:
        print("invalid input")


def main():
    while True:
        ask_option()
        choice = input("make your choice -> ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Thank you. Good bye.")
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()
