"""
File Name: user.py
Authors: 
Date: February 9, 2024
Description: This file contains the Task Class
"""

"""
Task Class :
Attributes:
    * name (str): username
    * toDoList (ToDoList) : user's tasks
"""

############# Modules Section #############
from To_Do_List import ToDoList
#######################################

class User:
    def __init__(self, name:str):
        self.name = name
        self.toDoList = ToDoList()