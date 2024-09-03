#!/usr/bin/python3
"""Amodule to query an api and return a json file"""

import requests
from sys import argv
from json import dumps


def get_name(url):
    """To get the name of the user"""
    response = requests.get(url)
    response = response.json()
    return response.get('username'), response.get('id')


def get_task(url):
    """To get the number of tasks done by the user"""
    response = requests.get(url)
    response = response.json()
    comp_list = []
    # Get the completed tasks and total number of tasks
    for a in response:
        status = [a.get('completed'), a.get('title')]
        comp_list.append(status)
    # Return a tuble containing the completed, total and names of task
    return comp_list


if __name__ == '__main__':
    mydict = {}
    for a in range(11):
        # define the urls
        url_user = f"https://jsonplaceholder.typicode.com/users/{a}"
        url_task = f"https://jsonplaceholder.typicode.com/todos?userId={a}"
        # get the relevant data
        u_name, u_id = get_name(url_user)
        tasks = get_task(url_task)

        # create the dictionary
        mydict[a] = []
        for task in tasks:
            mydict[a].append({
                'task': task[1],
                'completed': task[0],
                'username': u_name}
            )
    # save the output to a file
    with open(f"todo_all_employees.json", mode='a', encoding='utf-8') as File:
            File.write(dumps(mydict))
