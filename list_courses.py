#!/usr/bin/python3
from tabulate import tabulate

def display_course_list():
    """
    Display the list of courses from the file.
    """
    with open('course_list.txt', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    display_course_list()
