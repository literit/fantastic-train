#introduction to program?
 import collections
from typing import OrderedDict
from prettytable import PrettyTable

tasks={}
tasknumber = 0
def askfortasks():
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Continue to task order")
    action = input(":")
    if action == "1":
        addtask()
    elif action == "2":
        deletetask()
    elif action == "3":
        #returns list of tasks
        return tasks
    else:
        print("Invalid input")
        askfortasks()
def addtask():
    global tasknumber
    if tasknumber == 10:
        print("You have reached the maximum number of tasks.")
        askfortasks()
    print("What task would you like to add?")
    task = input(":")
    print("What is the difficulty of the task?")
    difficulty = input(":")
    global tasks
    tasks[tasknumber]= [difficulty, task]
    print("Task added.")
    tasknumber += 1
    askfortasks()
def deletetask():
    print("What task would you like to delete?")
    task = input(":")
    if task in tasks:
        del tasks[task]
        print("Task deleted.")
        tasknumber -= 1
    else:
        print("Task not found.")
    askfortasks()
askfortasks()
#order dictionary by its values
tasks = dict(OrderedDict(sorted(tasks.values())))
#makes a table of tasks using prettytable
table = PrettyTable()
table.field_names = ["Task", "Difficulty"]
for i in tasks:
    table.add_row([str(tasks[i]), i])
print(table)
