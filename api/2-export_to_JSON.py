#!/usr/bin/python3
"""
This is conversion to JSON
"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys
    
    argument = sys.argv[1]
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
    TASK_TITLE = task.get('title')
    USER_ID = users_response.json()[0]['id']
    USERNAME = users_response.json()[0]['username']

    details_dict = {argument: []}

    for task in tasks: 
        TASK_COMPLETED_STATUS = task['completed']
        TASK_TITLE = task['title']
        details_list = {"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS, "username": USERNAME}
      #  print(details_list)
        details_dict[argument].append(details_list)
        with open(f"{argument}.json", "w") as json_file:
            json.dump(details_dict, json_file)        
    print(details_dict)
