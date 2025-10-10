# -*- coding: utf-8 -*-

"""
Source code for mock up testing examples.
"""
import subprocess
import time

# pylint: disable=import-error
import requests


# 01
def fetch_data_from_api(url):
    """Fetches data from an external API using the requests library."""
    response = requests.get(url, timeout=10)
    return response.json()


# 02
def read_data_from_file(filename):
    """Read data from a file."""
    try:
        with open(filename, encoding="utf-8") as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        raise e


# 03
def execute_command(command):
    """Execute a command in a subprocess."""
    try:
        result = subprocess.run(command, capture_output=True, check=False, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise e


# 04
def perform_action_based_on_time():
    """Perform an action based on the current time."""
    current_time = time.time()
    if current_time < 10:
        return "Action A"

    return "Action B"
