#!/usr/bin/python3

"""
Exportting data to csv format
"""

import csv
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
    
    filename = user_id + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        
        for todo in todos.json():
            if todo.get('userId') == int(user_id):
                writer.writerow([user_id, emp_name, str(todo.get(
                    "completed")), todo.get('title')])