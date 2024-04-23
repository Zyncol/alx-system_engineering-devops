#!/usr/bin/python3

"""
Python script exporting data in JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    levrow = []
    feedback = get('https://jsonplaceholder.typicode.com/users')
    sdata = feedback.json()

    ndict1 = {}

    for k in sdata:

        levrow = []
        for i in data:

            ndict2 = {}

            if k['id'] == i['userId']:

                ndict2['username'] = k['username']
                ndict2['task'] = i['title']
                ndict2['completed'] = i['completed']
                levrow.append(ndict2)

        ndict1[k['id']] = levrow

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(ndict1)
        f.write(json_obj)
