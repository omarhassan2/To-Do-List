"""
File Name: main.py
Authors: - - Omar
Date: February 9, 2024
Description: This file contains implementations of the command-line interface(CLI) 
             for user interaction and utilizes functions.
"""


############# Modules Section #############
from Task import Task
from To_Do_List import ToDoList
import os
#######################################

"""
The main function that serves as the entry point for the To-Do List application.
"""
def main():
    # Creat an object from ToDoList
    todo_list = ToDoList()

    while True:
        # Implement your command-line interface for user interaction
        # Use functions from ToDoList class to perform operations on the task list
        pass

if __name__ == "__main__":
    main()