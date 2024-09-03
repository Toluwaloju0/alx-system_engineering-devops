#!/usr/bin/python3
"""Amodule to query an api and return a csv file"""

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
    # define the urls
    url_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    url_task = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
    # get the relevant data
    u_name, u_id = get_name(url_user)
    tasks = get_task(url_task)

    # save the output to a file
    for task in tasks:
        mylist = [u_id, u_name, task[0], task[1]]
        print(mylist)
        with open(f"{argv[1]}.csv", mode='a', encoding='utf-8') as File:
            File.write(dumps(mylist))
