#!/usr/bin/python3

class Student:
    """
    Represents a student with an email, names, registered courses, and GPA.
    """
    
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}  # {course_name: (grade, credits)}
        self.GPA = 0

    def register_for_course(self, course_name, grade, credits):
        """
        Register a grade and credits for a course.
        """
        self.courses_registered[course_name] = (grade, credits)
        self.calculate_GPA()

    def calculate_GPA(self):
        """
        Calculate GPA based on registered courses.
        """
        total_points = 0
        total_credits = 0
        for grade, credits in self.courses_registered.values():
            total_points += grade * credits
            total_credits += credits
        self.GPA = total_points / total_credits if total_credits > 0 else 0

    def to_dict(self):
        """
        Convert student data to a dictionary for easy saving.
        """
        return {
            'email': self.email,
            'names': self.names,
            'courses_registered': self.courses_registered,
            'GPA': self.GPA
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Student instance from a dictionary.
        """
        student = Student(data['email'], data['names'])
        student.courses_registered = data['courses_registered']
        student.GPA = data['GPA']
        return student
