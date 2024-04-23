#!/usr/bin/python3
"""
a script that, using a REST API, for a given employee ID,
returns information about TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    feedback = get('https://jsonplaceholder.typicode.com/users')
    sdata = feedback.json()

    for e in sdata:
        if e.get('id') == int(argv[1]):
            employee = e.get('name')

    for e in data:
        if e.get('userId') == int(argv[1]):
            total += 1

            if e.get('completed') is True:
                completed += 1
                tasks.append(e.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))

    for e in tasks:
        print("\t {}".format(e))
