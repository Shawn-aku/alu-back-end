#!/usr/bin/python3
"""Exports an employee's tasks to JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )

    employee = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    tasks = []

    for task in todos:
        task_data = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee["username"]
        }
        tasks.append(task_data)

    data = {
        employee_id: tasks
    }

    filename = "{}.json".format(employee_id)

    with open(filename, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file)
