#!/usr/bin/python3
"""For a given employee ID, returns information about
TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    uId = sys.argv[1]
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(uId))
    name = usr.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    tTask = 0
    donee = 0

    for task in todos.json():
        if task.get('uId') == int(uId):
            tTask += 1
            if task.get('donee'):
                donee += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, donee, tTask))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('uId') == int(uId) and task.get('donee')]))
