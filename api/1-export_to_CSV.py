#!/usr/bin/python3
"""Exports an employee's tasks to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )

    employee = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                employee["username"],
                task["completed"],
                task["title"]
            ])
