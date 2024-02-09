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
    * priority    (int) : The priority level[1 - 2 - 3] of the task (default is 3).
    * additional_details (str) : Additional details about the task (default is None).
Functions:
    * mark_as_completed
"""
class Task:
    def __init__(task, description : str, due_date=None, priority=3, additional_details=None):
        task.description = description
        task.due_date = due_date
        task.priority = priority
        task.additional_details = additional_details
        task.completed = False # All tasks must be False until mark as complete



    """
    # @author :
    # @description : Marks a task as completed.
    # @param : task (Task): The Task object to be marked as completed.
    # @return :
    """
    def mark_as_completed(task):
        task.completed = True