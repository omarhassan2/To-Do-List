"""
File Name: main.py
Authors: Tasnem - Marwan - Hager - Hassan - Nancy - Omar 
Date: February 9, 2024
Description: This file contains the main application (Command Line Interface)
"""

"""
Functions:
    * clear_screen
    * create_user_tasks_file
    * delete_user_tasks_file
    * load_user_tasks
    * save_user_tasks
    * user_menu
    * add_user
    * delete_user
    * display_users
    * login
    * main

"""

############# Modules Section #############
from Task import Task
from To_Do_List import ToDoList
from User import User
import time
import os
from colorama import init, Fore, Style
import json
import os
#######################################

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def create_user_tasks_file(user: User):
    """
    Create a JSON file for the user's tasks.

    Parameters:
    - user (User): The User object.

    Returns:
    - None
    """
    filename = f"{user}_tasks.json"
    with open(filename, "w") as tasks_file:
        json.dump([], tasks_file)  # Initialize with an empty list

def delete_user_tasks_file(user : User):
    """
    Delete the JSON file for the user's tasks.

    Parameters:
    - user (User): The User object.

    Returns:
    - None
    """
    filename = f"{user}_tasks.json"
    if os.path.exists(filename):
        os.remove(filename)

def load_user_tasks(user : User):
    """
    Load tasks from the user's JSON file.

    Parameters:
    - user (User): The User object.

    Returns:
    - List of tasks (list)
    """
    filename = f"{user}_tasks.json"
    if os.path.exists(filename):

        try:
            with open(filename, "r") as tasks_file:

                data = json.load(tasks_file)

                tasks = [Task(**task) for task in data]

            return tasks
        
        except json.JSONDecodeError as e:

            print(f"{Fore.RED}Error decoding JSON from '{filename}': {e}")

    return []

def save_user_tasks(user :User, tasks):
    """
    Save tasks to the user's JSON file.

    Parameters:
    - user (User): The User object.
    - tasks (list): List of tasks.

    Returns:
    - None
    """
    filename = f"{user}_tasks.json"
    try:
        with open(filename, "w") as tasks_file:
            
            tasks_data = [task.to_dict() for task in tasks]

            json.dump(tasks_data, tasks_file, indent=2)

        print(f"{Fore.GREEN}Data successfully saved to {filename}")

    except IOError as e:
        print(f"{Fore.RED}Error writing to '{filename}': {e}")

def template_menu():
    print(f"{Fore.LIGHTGREEN_EX}" + "-"*25)
    print(f"{Fore.LIGHTGREEN_EX}" + "|       User Menu       |")
    print(f"{Fore.LIGHTGREEN_EX}" + "-"*25)
    print(f"{Fore.LIGHTMAGENTA_EX}1." + Style.RESET_ALL + " Add Task")
    print(f"{Fore.LIGHTMAGENTA_EX}2." + Style.RESET_ALL + " Mark Task as Completed")
    print(f"{Fore.LIGHTMAGENTA_EX}3." + Style.RESET_ALL + " Delete Task")
    print(f"{Fore.LIGHTMAGENTA_EX}4." + Style.RESET_ALL + " View Tasks")
    print(f"{Fore.LIGHTMAGENTA_EX}5." + Style.RESET_ALL + " Logout")
    print(f"{Fore.LIGHTGREEN_EX}" + "-"*25)

def user_menu(logged_user):
    """
    Displays the user menu for managing tasks.

    Parameters:
    - logged_user (User): The logged-in User object.

    Returns:
    - None
    """
    # Load user tasks when logging in
    logged_user.toDoList.tasks = load_user_tasks(logged_user)

    template_menu()

    while True:
        for char in "Enter your choice (1-5):":
            print(char, end='', flush=True)
            time.sleep(0.03)
        choice = input()

        if choice == "1":
            os.system("cls")
            # Get task details from the user and add the task
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            
            while True:

                priority_input = input("Enter priority (1-Low/2-Medium/3-High): ")

                if priority_input in ["1", "2", "3"]:
                    priority = ["Low", "Medium", "High"][int(priority_input) - 1]
                    break
                
                else:
                    print(f"{Fore.RED}Invalid priority input. Please enter 1, 2, or 3.")


            additional_details = input("Enter additional details (optional): ")

            new_task = Task(description, due_date, priority, additional_details)
            logged_user.toDoList.add_task(new_task)

            # Save tasks after adding
            save_user_tasks(logged_user, logged_user.toDoList.tasks)

            time.sleep(1)
            os.system("cls")
            template_menu()

        elif choice == "2":
            os.system("cls")

            # Mark a task as completed
            try:
                if logged_user.toDoList.view_tasks() != -1:
                    print(f"{Fore.LIGHTGREEN_EX}" + "-"*25)
                    task_index = int(input("Enter the index of the task to mark as completed: "))
                    logged_user.toDoList.mark_task_as_completed(task_index - 1)
            except IndexError:
                print(f"{Fore.RED}Invalid index. Please enter a number between 1 and {len(logged_user.toDoList.tasks)}.")

            # Save tasks after marking as completed
            save_user_tasks(logged_user, logged_user.toDoList.tasks)

            time.sleep(1)
            os.system("cls")
            template_menu()

        elif choice == "3":
            os.system("cls")

            # Delete a task
            logged_user.toDoList.view_tasks()
            
            print(f"{Fore.LIGHTGREEN_EX}" + "-"*25)
            task_index = int(input(f"{Fore.YELLOW}Enter the index of the task to delete: "))
            logged_user.toDoList.delete_task(task_index - 1)

            # Save tasks after deletion
            save_user_tasks(logged_user, logged_user.toDoList.tasks)

            time.sleep(1)
            os.system("cls")
            template_menu()

        elif choice == "4":
            os.system("cls")

            # View tasks
            logged_user.toDoList.view_tasks()

            username = input(f"\n{Fore.YELLOW}" + "type 'back' to return to the main menu: ")

            if username.lower() == 'back':
                os.system("cls")
                template_menu()


        elif choice == "5":
            # Logout and return to the main menu

            # Save tasks before logging out
            save_user_tasks(logged_user, logged_user.toDoList.tasks)

            print(f"{Fore.BLUE}Logging out...")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please enter a number between 1 and 5.")

def add_user(users_list, user_name):
    """
    Adds a new user to the list of users.

    Parameters:
    - users_list (list): List of User objects.
    - user_name (str): Name of the new user.

    Returns:
    - None
    """
    try:
        new_user = User(user_name)
        users_list.append(new_user)
        print(f"{Fore.GREEN}User '{user_name}' has been added.")
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}")

def delete_user(users_list, user_name):
    """
    Deletes a user from the list of users.

    Parameters:
    - users_list (list): List of User objects.
    - user_name (str): Name of the user to be deleted.

    Returns:
    - User object if deleted, None otherwise.
    """
    try:
        for user in users_list:
            if user.name == user_name:

                users_list.remove(user)
                print(f"{Fore.YELLOW}User '{user_name}' has been deleted.")
                return user
            
        raise ValueError(f"{Fore.RED}User '{user_name}' not found.")
    
    except ValueError as e:

        print(f"{Fore.RED}Error: {e}")
        return None

def display_users(users_list):
    """
    Displays the list of users in a box shape with lightcyan color.

    Parameters:
    - users_list (list): List of User objects.

    Returns:
    - None
    """
    print(f"{Fore.CYAN}Users List")
    for user in users_list:
        print(f"{Fore.CYAN}| {user.name} ", end='')
    print()

def login(users_list):
    """
    Handles user login by prompting for a username.

    Parameters:
    - users_list (list): List of User objects.

    Returns:
    - User object if login is successful, None otherwise.
    """
    while True:
        try:
            username = input(f"\n{Fore.YELLOW}" + "Enter your username to login (or type 'back' to return to the main menu): ")

            if username.lower() == 'back':
                return None

            user = next((u for u in users_list if u.name == username), None)

            if not user:
                raise ValueError(f"User '{username}' not found. Please try again.")

            print(Fore.GREEN + "Welcome, {}!".format(username) + Style.RESET_ALL)
            return user
        
        except ValueError as e:
            print(f"{Fore.RED}Error: {e}")


def template():
    print(f"\n\t\t\t{Fore.LIGHTGREEN_EX}" + "-" * 40)
    print(f"{Fore.LIGHTGREEN_EX}" + "\t\t\t|   Welcome to To-Do List Application  |")
    print(f"\t\t\t{Fore.LIGHTGREEN_EX}" + "-" * 40)

    print(f"{Fore.LIGHTGREEN_EX}" + "-"*17)
    print(f"{Fore.LIGHTGREEN_EX}" + "|   Main Menu   |")
    print(f"{Fore.LIGHTGREEN_EX}" + "-"*17)
    
    print(f"{Fore.LIGHTMAGENTA_EX}1." + Style.RESET_ALL + " Add User")
    print(f"{Fore.LIGHTMAGENTA_EX}2." + Style.RESET_ALL + " Delete User")
    print(f"{Fore.LIGHTMAGENTA_EX}3." + Style.RESET_ALL + " Login")
    print(f"{Fore.LIGHTMAGENTA_EX}4." + Style.RESET_ALL + " Exit")
    print(f"{Fore.LIGHTGREEN_EX}" + "-"*17)


def main():
    # List to store User objects
    users_list = []

    template()

    while True:
        

        # display_users(users_list)

        
        for char in "Enter your choice (1-4):":
            print(char, end='', flush=True)
            time.sleep(0.03)
        choice = input()

        if choice == "1":
            os.system("cls")
            print(f"\n\t\t\t{Fore.LIGHTGREEN_EX}" + "-"*33)
            print(f"{Fore.LIGHTGREEN_EX}" + "\t\t\t|   Welcome to Registration Page  |")
            print(f"\t\t\t{Fore.LIGHTGREEN_EX}" + "-" * 33)

            user_name = input(f"\n{Fore.YELLOW}" + "Enter your username: ")
            add_user(users_list, user_name)

            time.sleep(1)
            os.system("cls")
            template()

        elif choice == "2":
            os.system("cls")
            print(f"\n\t\t\t{Fore.LIGHTGREEN_EX}" + "-" * 35)
            print(f"{Fore.LIGHTGREEN_EX}" + "\t\t\t|   Welcome to Deleting Page  |")
            print(f"\t\t\t{Fore.LIGHTGREEN_EX}" + "-" * 35)

            print(f"{Fore.LIGHTGREEN_EX}" + "-" * 20)
            display_users(users_list)
            print(f"{Fore.LIGHTGREEN_EX}" + "-" * 20)

            user_name = input(f"\n{Fore.YELLOW}" + "Enter the name of the user you want to delete: ")
            delete_user(users_list, user_name)
            delete_user_tasks_file(user_name)

            time.sleep(1)
            os.system("cls")
            template()

        elif choice == "3":
            os.system("cls")
            print(f"\n\t\t\t{Fore.LIGHTGREEN_EX}" + "-" * 28)
            print(f"{Fore.LIGHTGREEN_EX}" + "\t\t\t|   Welcome to Login Page  |")
            print(f"\t\t\t{Fore.LIGHTGREEN_EX}" + "-" * 28)

            logged_user = login(users_list)

            if logged_user:
                user_menu(logged_user)

            time.sleep(1)
            os.system("cls")
            template()

        elif choice == "4":
            print("Exiting To-Do List Application.")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()