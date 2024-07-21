#!/usr/bin/python3

class Student:
    """
    A class to represent a student.

    Attributes:
        email (str): The email address of the student.
        names (str): The full name of the student.
        courses_registered (dict): A dictionary of courses with associated grades and credits.
        GPA (float): The calculated Grade Point Average of the student.
    """

    def __init__(self, email, names):
        """
        Initializes a new student with the given email and names.

        Args:
            email (str): The email address of the student.
            names (str): The full name of the student.
        """
        self.email = email
        self.names = names
        self.courses_registered = {}  # Dictionary to store course names and grades
        self.GPA = 0.0
    
    def calculate_GPA(self):
        """
        Calculates and updates the GPA based on registered courses and grades.
        """
        if not self.courses_registered:
            self.GPA = 0.0
            return
        
        total_points = 0
        total_credits = 0
        for course, (grade, credits) in self.courses_registered.items():
            total_points += grade * credits
            total_credits += credits
        
        self.GPA = total_points / total_credits
    
    def register_for_course(self, course, grade, credits):
        """
        Registers the student for a course with a given grade and credits.

        Args:
            course (str): The name of the course.
            grade (float): The grade received in the course.
            credits (int): The number of credits for the course.
        """
        self.courses_registered[course] = (grade, credits)
        self.calculate_GPA()
