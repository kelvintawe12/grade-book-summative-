#!/usr/bin/python3
from tabulate import tabulate

def display_student_list():
    """
    Display the list of students from the file.
    """
    with open('student_list.txt', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    display_student_list()
