#!/usr/bin/python3

"""
This is a Python script to export data in the JSON format.
	Records all tasks from all employees
"""

import json
import requests
import sys

if __name__ == "__main__":
    # getting the userid from terminal
    # user_id = sys.argv[1]
    # getting a user
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    # getting employee name, by parsing it to a python object
    # emp_name = user.json().get("username")
    # getting the todos
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    all_users_todo = {}
    for user in users.json():
        all_tasks = []
        for todo in todos.json():
            if todo.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                             "task": todo.get('title'),
                             "completed": todo.get('completed')}
                all_tasks.append(task_dict)
        all_users_todo[user.get('id')] = all_tasks
    # writing the data to a json file
    with open("todo_all_employees.json", mode='w') as f:
        json.dump(all_users_todo, f)

    # Another way.
    # filename = user_id + '.json'
    # with open(filename, mode='w') as f:
    #     json.dump(all_users_todo, f)
