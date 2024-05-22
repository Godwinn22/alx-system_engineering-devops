#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her todo list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # getting the userid from terminal
    user_id = sys.argv[1]
    # getting a user
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    # getting employee name, by parsing it to a python object
    emp_name = user.json().get("name")
    # getting the todos
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    total_tasks = 0
    tasks_completed = 0

    for todo in todos.json():
        if todo.get('userId') == int(user_id):
            total_tasks += 1
            if todo.get('completed'):
                tasks_completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(emp_name, tasks_completed, total_tasks))

    # Assuming `todo.json()` returns a list of tasks
    for todo in todos.json():
        if todo.get('userId') == int(user_id
                                     ) and todo.get('completed'):
            # tasks_completed += 1
            print("\t" + todo.get('title'))
