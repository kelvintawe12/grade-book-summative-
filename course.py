#!/usr/bin/python3

class Course:
    """
    A class to represent a course.

    Attributes:
        name (str): The name of the course.
        trimester (str): The trimester in which the course is offered.
        credits (int): The number of credits the course is worth.
    """

    def __init__(self, name, trimester, credits):
        """
        Initializes a new course with the given name, trimester, and credits.

        Args:
            name (str): The name of the course.
            trimester (str): The trimester in which the course is offered.
            credits (int): The number of credits the course is worth.
        """
        self.name = name
        self.trimester = trimester
        self.credits = credits
