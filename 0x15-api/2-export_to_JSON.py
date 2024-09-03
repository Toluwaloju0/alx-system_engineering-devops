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
    # define the urls
    url_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    url_task = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
    # get the relevant data
    u_name, u_id = get_name(url_user)
    tasks = get_task(url_task)

    # create the dictionary
    mydict = {argv[1]: []}
    for task in tasks:
        mydict[argv[1]].append({
            'task': task[1],
            'completed': task[0],
            'username': u_name}
        )
    # save the output to a file
    with open(f"{argv[1]}.json", mode='a', encoding='utf-8') as File:
        File.write(dumps(mydict))
