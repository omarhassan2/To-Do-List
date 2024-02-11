"""
File Name: Task.py
Authors: Omar
Date: February 9, 2024
Description: This file contains the Task Class
"""


"""
Task Class :
Attributes:
    * description (str) : The description of the task.
    * completed   (bool): The completion status of the task (default is False).
    * due_date    (str) : The due date of the task (default is None).
    * priority    (str) : The priority level[1(High) - 2(Medium) - 3(Low)] of the task (default is 3).
    * additional_details (str) : Additional details about the task (default is None).
Functions:
    * mark_as_completed
"""

############# Modules Section #############
from colorama import init, Fore, Style
###########################################

init(autoreset=True)


class Task:
    def __init__(task, description : str,completed=False, due_date=None, priority="Low", additional_details=None):
        task.description = description
        task.due_date = due_date
        task.priority = priority
        task.additional_details = additional_details
        task.completed = completed # All tasks must be False until mark as complete



    """
    # @author : Marwan
    # @description : Marks a task as completed.
    """
    def to_dict(self):
        """
        Convert Task object to a dictionary for serialization.
        """

        return {
            "description": str(self.description),
            "due_date": str(self.due_date),
            "priority": str(self.priority),
            "additional_details": str(self.additional_details),
            "completed": str(self.completed)
        }
    
    """
    # @author :
    # @description : Marks a task as completed.
    """
    def mark_as_completed(self):
        self.completed = True

    """
    # @author : Omar
    # @description : Set the due date of the task.
    # @param : date (str): The due date of the tas
    """
    def set_due_date(task, date:str):
        task.due_date = date


    """
    # @author : Omar
    # @description : Set the due date of the task.
    # @param : date (str): The due date of the tas
    """
    def set_additional_details(task, additional_details:str):
        task.additional_details = additional_details



    """
    # @author : Omar
    # @description : Set the due date of the task.
    # @param : date (str): The due date of the tas
    """
    def get_priority(self):
        return self.priority


    """
    # @author : Omar
    # @description : show how Task class will be printed.
    """
    def __str__(self):
        return (f"Task:\n"
                f"  Description: {self.description}\n"
                f"  Due Date: {self.due_date}\n"
                f"  Priority: {self.priority}\n"
                f"  Additional Details: {self.additional_details}\n"
                f"  Completed: {self.completed}")