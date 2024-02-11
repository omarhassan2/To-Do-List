"""
File Name: To_Do_List.py
Authors: Tasnem - Marwan - Hager - Hassan - Nancy - Omar 
Date: February 9, 2024
Description: This file contains the To-Do-List Class
"""

import json
from colorama import init, Fore, Style

init(autoreset=True)

list_of_tasks= []

"""
ToDoList Class :
Attributes:
    * tasks (list) : list of tasks(To-Do List).
Functions:
    * add_task                  1       --> Hassan
    * delete_task               2       --> Tasnem
    * mark_task_as_completed    3       --> Hager
    * set_due_date              4       --> Nancy
    * set_additional_details    5       --> Nancy
    * view_tasks                6       --> Hassan
    * sort_by_priority          7       --> Tasnem
    * sort_by_due_date          8       --> Hager
    * save_to_json              9       --> Marwan
    * load_from_json            10      --> Marwan
"""

############# Modules Section #############
from Task import Task
#######################################

class ToDoList:
    def __init__(self):
        # Initializes an empty To-Do List with no tasks.
        self.tasks = []




    """
    # @author :
    # @description :  Adds a task to the To-Do List.
    # @param :  task (Task): The Task object to be added to the To-Do List.
    # @return :
    """
    def add_task(self, task: Task):

        try:
            self.tasks.append(task)

        except ValueError as e:
            print(f"{Fore.RED}{e}, Failed to add task.")    



    """
    # @author :
    # @description : Deletes a specific task from the To-Do List.
    # @param : task_index (int): The index of the task to be deleted.
    # @return :
    """    
    def delete_task(self, task_index:int):

        try:
            TaskToDelete = list(self.tasks)[task_index]
            self.tasks.remove(TaskToDelete)

            print(f"{Fore.YELLOW}Task {TaskToDelete} has been removed.")

        except IndexError:
            raise IndexError(f"{Fore.RED}Invalid task index. No task found at the provided index.")



    """
    # @author :
    # @description : Marks a specific task in the To-Do List as completed.
    # @param : task_index (int): The index of the task to be completed.
    # @return :
    """
    def mark_task_as_completed(self, task_index:int):
        if not self.tasks:
            print(f"{Fore.RED}Error: No tasks to complete.")
            return
        task = Task(self.tasks[task_index])
        task.mark_as_completed()



    """
    # @author :
    # @description : Sets the due date for a specific task in the To-Do List.
    # @param task_index (int): The index of the task for which to set the due date.
    # @param due_date (str or None): The due date to be set for the task. Pass None if no due date is needed.
    """
    def set_due_date(self, task_index:int, due_date:str):
        if not self.tasks:
            print(f"{Fore.RED}Error: No tasks to set due date for.")
            return
        task =Task(self.tasks[task_index])
        task.set_due_date(due_date)



    """
    # @author :
    # @description : Sets additional details for a specific task in the To-Do List.
    # @param task_index (int): The index of the task for which to set additional details.
    # @param additional_details (str or None): The additional details to be set for the task.
    """
    def set_additional_details(self, task_index:int, additional_details:str):
        if not self.tasks:
            print("Error: No tasks to set additional details for.")
            return
        task = Task(self.tasks[task_index])
        task.set_additional_details(additional_details)



    """
    # @author :
    # @description : Displays the list of tasks in the To-Do List.
    """
    def view_tasks(self):
        if not self.tasks:
            print(f"{Fore.RED}The To-Do List is empty.")
            return -1
        else:
            print("Tasks in the To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}.{task}")



    """
    # @author :
    # @description : Sorts the tasks in the To-Do List based on priority level.
    """
    def sort_by_priority(self):
        # Write your code here 
        # Note that the next line is just my suggestion to sort by priority @Marwan Abdelmoneim
        # TODO make a dictionary here for a priority level and assign numbers to each priority
        # Example: priority_order = {"Low": 1, "Medium": 2, "High": 3}
       priority_order = {"Low": 1, "Medium": 2, "High": 3}  # Assign numerical values to priorities
       self.tasks.sort(key = lambda task: priority_order.get(task.get_priority()), reverse=True) 


    """
    # @author :
    # @description : Here we are saving the data from the list_of_tasks variable to the JSON file.
    # @param : filename (str): The name of the JSON file to save the To-Do List.
    # @Functionality: The function starts with opening the json file in write mode
                      then writing the task passed to it into json file.
    """
    def save_to_json(task, filename:str):
        try:
            with open(filename, "w") as tasks_file:
                json.dump(task, tasks_file, indent=2)
            print(f"Data successfully saved to {filename}")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except IOError as e:
            print(f"Error writing to '{filename}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")



    """
    # @author :
    # @description : Here we are loading the data from the JSON file into the list_of_tasks variable
    # @param : filename (str): The name of the JSON file to load tasks from.
    # @Functionality: The function starts with opening the json file in read mode
                      and loads the data into the list_of_tasks variable.
    """
    def load_from_json(self, filename:str):
        try:
            with open(filename, "r") as tasks_file:
                data = json.load(tasks_file)

            for task in data:
                list_of_tasks.append(task)
            print(f"Data successfully loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except IOError as e:
            print(f"Error reading from '{filename}': {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from '{filename}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")