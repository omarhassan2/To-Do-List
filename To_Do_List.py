"""
File Name: To_Do_List.py
Authors: Tasnem - Marwan - Hager - Hassan - Nancy - Omar 
Date: February 9, 2024
Description: This file contains the To-Do-List Class
"""


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
    def add_task(self, task:Task):
        # Write your code here
        pass
    


    """
    # @author :
    # @description : Deletes a specific task from the To-Do List.
    # @param : task_index (int): The index of the task to be deleted.
    # @return :
    """    
    def delete_task(self, task_index:int):
        # Write your code here
        pass



    """
    # @author :
    # @description : Marks a specific task in the To-Do List as completed.
    # @param : task_index (int): The index of the task to be completed.
    # @return :
    """
    def mark_task_as_completed(self, task_index:int):
        # Write your code here
        pass



    """
    # @author :
    # @description : Sets the due date for a specific task in the To-Do List.
    # @param task_index (int): The index of the task for which to set the due date.
    # @param due_date (str or None): The due date to be set for the task. Pass None if no due date is needed.
    # @return :
    """
    def set_due_date(self, task_index:int, due_date:str):
        # Write your code here
        pass



    """
    # @author :
    # @description : Sets additional details for a specific task in the To-Do List.
    # @param task_index (int): The index of the task for which to set additional details.
    # @param additional_details (str or None): The additional details to be set for the task.
    # @return :
    """
    def set_additional_details(self, task_index:int, additional_details:str):
        # Write your code here
        pass



    """
    # @author :
    # @description : Displays the list of tasks in the To-Do List.
    # @param :
    # @return :
    """
    def view_tasks(self):
        # Write your code here
        pass



    """
    # @author :
    # @description : Sorts the tasks in the To-Do List based on priority level.
    # @param :
    # @return :
    """
    def sort_by_priority(self):
        # Write your code here
        pass



    """
    # @author :
    # @description : Sorts the tasks in the To-Do List based on due date.
    # @param :
    # @return :
    """
    def sort_by_due_date(self):
        # Write your code here
        pass



    """
    # @author :
    # @description : Saves the list of tasks to a JSON file.
    # @param : filename (str): The name of the JSON file to save the To-Do List.
    # @return :
    """
    def save_to_json(self, filename:str):
        # Write your code here
        pass



    """
    # @author :
    # @description : Loads tasks from a JSON file and updates the task list.
    # @param : filename (str): The name of the JSON file to load tasks from.
    # @return :
    """
    def load_from_json(self, filename:str):
        # Write your code here
        pass