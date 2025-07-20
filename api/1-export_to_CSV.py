#!/usr/bin/python3
"""
This is conversion to CSV
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
    print(tasks)
    for task in tasks:
        TASK_COMPLETED_STATUS = task['completed']
        TASK_TITLE = task['title']
        with open(f'{argument}.csv', 'a', newline='') as user_id:
            details_writer = csv.writer(user_id, quoting=csv.QUOTE_ALL)

            details_writer.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
        

