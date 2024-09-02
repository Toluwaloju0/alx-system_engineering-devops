#!/usr/bin/python3
"""A module to query an api"""

import requests
from sys import argv


def get_name(url):
    """To get the name of the user"""
    response = requests.get(url)
    response = response.json()
    return response.get('name')


def get_task(url):
    """To get the number of tasks done by the user"""
    response = requests.get(url)
    response = response.json()
    total = 0
    comp = 0
    comp_list = []
    # Get the completed tasks and total number of tasks
    for a in response:
        total += 1
        if a.get('completed'):
            comp += 1
            comp_list.append(a['title'])
    # Return a tuble containing the completed, total and names of task
    return comp, total, comp_list


if __name__ == '__main__':
    # define the urls
    url_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    url_task = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
    # get the relevant data
    e_name = get_name(url_user)
    comp, total, tasks = get_task(url_task)

    # Print the output
    print(f"Employee {e_name} is done with tasks({comp}/{total}):")
    for task in tasks:
        print(f"\t {task}")
