#!/usr/bin/python3

"""
Python script exporting data in JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    lev = []
    feedback = get('https://jsonplaceholder.typicode.com/users')
    sdata = feedback.json()

    for e in sdata:
        if e['id'] == int(argv[1]):
            us_name = e['username']
            id_no = e['id']

    lev = []

    for e in data:
        new_dict = {}

        if e['userId'] == int(argv[1]):
            new_dict['username'] = us_name
            new_dict['task'] = e['title']
            new_dict['completed'] = e['completed']
            lev.append(new_dict)

    final_dict = {}
    final_dict[id_no] = lev
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
