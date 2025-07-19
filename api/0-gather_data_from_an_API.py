#!/usr/bin/python3
import requests
import json
import sys

todos_endpoint = 'https://jsonplaceholder.typicode.com/todos'
todos_params = {'userId': sys.argv[1]}

users_endpoint = 'https://jsonplaceholder.typicode.com/users'
users_params = {'id' : sys.argv[1]}

users_response = requests.get(users_endpoint, users_params)

todos_response = requests.get(todos_endpoint, todos_params)
tasks = todos_response.json()

NUMBER_OF_DONE_TASKS = 0
for task in tasks:
    if task.get('completed') == 1:
        NUMBER_OF_DONE_TASKS += 1
    else:
        NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS

TOTAL_NUMBER_OF_TASKS = len(tasks)


employee_details = users_response.json()
EMPLOYEE_NAME = employee_details[0]['name']

print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
for task in tasks:
    TASK_TITLE = task.get('title')
    print(f"\t {TASK_TITLE}")







