#!/usr/bin/python3
"""Exports all employees' tasks to JSON format."""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    all_tasks = {}

    for user in users:
        user_id = str(user["id"])
        username = user["username"]
        all_tasks[user_id] = []

        for task in todos:
            if task["userId"] == user["id"]:
                task_data = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                all_tasks[user_id].append(task_data)

    with open(
        "todo_all_employees.json",
        mode="w",
        encoding="utf-8"
    ) as json_file:
        json.dump(all_tasks, json_file)
