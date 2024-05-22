#!/usr/bin/python3

"""
This is a Python script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # getting the userid from terminal
    user_id = sys.argv[1]
    # getting a user
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    # getting employee name, by parsing it to a python object
    emp_name = user.json().get("username")
    # getting the todos
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    users_todo = {}
    all_tasks = []

    for todo in todos.json():
        if todo.get('userId') == int(user_id):
            task_dict = {"task": todo.get('title'), "completed": todo.get(
                'completed'), "username": user.json().get('username')}
            all_tasks.append(task_dict)

    users_todo[user_id] = all_tasks
    # writing the data to a json file
    with open("{}.json".format(user_id), 'w') as f:
        json.dump(users_todo, f)

    # Another way.
    # filename = user_id + '.json'
    # with open(filename, mode='w') as f:
    #     json.dump(users_todo, f)
