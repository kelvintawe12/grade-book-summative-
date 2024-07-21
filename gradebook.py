#!/usr/bin/python3
import json
from student import Student
from course import Course
from tabulate import tabulate

class GradeBook:
    """
    Manages students, courses, and their registrations.
    """
    
    def __init__(self):
        self.student_list = {}
        self.course_list = {}
        self.load_data()
        self.update_student_list_file()  # Ensure the file is created/updated at initialization
        self.update_course_list_file()   # Ensure the file is created/updated at initialization

    def add_student(self, student):
        """
        Add a new student to the grade book.
        """
        self.student_list[student.email] = student
        self.save_data()
        self.update_student_list_file()

    def add_course(self, course):
        """
        Add a new course to the grade book.
        """
        self.course_list[course.name] = course
        self.save_data()
        self.update_course_list_file()

    def register_student_for_course(self, student_email, course_name, grade, credits):
        """
        Register a student for a course with a given grade and credits.
        """
        if student_email in self.student_list and course_name in self.course_list:
            student = self.student_list[student_email]
            student.register_for_course(course_name, grade, credits)
            self.save_data()
            self.update_student_list_file()

    def calculate_GPA(self):
        """
        Update GPA for all students.
        """
        for student in self.student_list.values():
            student.calculate_GPA()
        self.save_data()

    def calculate_ranking(self):
        """
        Calculate and return a ranking of students by GPA.
        """
        return sorted(self.student_list.values(), key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, course_name, grade_range):
        """
        Search students by their grades in a specific course.
        """
        result = []
        for student in self.student_list.values():
            if course_name in student.courses_registered:
                grade, _ = student.courses_registered[course_name]
                if grade_range[0] <= grade <= grade_range[1]:
                    result.append(student)
        return result

    def generate_transcript(self, student_email):
        """
        Generate and return a transcript for a student.
        """
        student = self.student_list.get(student_email)
        if student:
            transcript = f"Transcript for {student.names} ({student.email}):\n"
            for course, (grade, credits) in student.courses_registered.items():
                transcript += f"- {course}: Grade = {grade}, Credits = {credits}\n"
            transcript += f"GPA = {student.GPA:.2f}"
            return transcript
        return "Student not found."

    def save_data(self):
        """
        Save student and course data to files.
        """
        with open('students.json', 'w') as f:
            json.dump({email: student.to_dict() for email, student in self.student_list.items()}, f)
        with open('courses.json', 'w') as f:
            json.dump({name: vars(course) for name, course in self.course_list.items()}, f)

    def load_data(self):
        """
        Load student and course data from files.
        """
        try:
            with open('students.json', 'r') as f:
                students_data = json.load(f)
                self.student_list = {email: Student.from_dict(data) for email, data in students_data.items()}
        except FileNotFoundError:
            self.student_list = {}

        try:
            with open('courses.json', 'r') as f:
                courses_data = json.load(f)
                self.course_list = {name: Course(**data) for name, data in courses_data.items()}
        except FileNotFoundError:
            self.course_list = {}

    def update_student_list_file(self):
        """
        Update the file that lists students and their details.
        """
        student_data = [
            [student.email, student.names, course, grade, credits]
            for student in self.student_list.values()
            for course, (grade, credits) in student.courses_registered.items()
        ]
        headers = ["Email", "Name", "Course", "Grade", "Credits"]
        with open('student_list.txt', 'w') as f:
            f.write(tabulate(student_data, headers=headers, tablefmt="grid"))

    def update_course_list_file(self):
        """
        Update the file that lists available courses.
        """
        course_data = [
            [course.name, course.trimester, course.credits]
            for course in self.course_list.values()
        ]
        headers = ["Course Name", "Trimester", "Credits"]
        with open('course_list.txt', 'w') as f:
            f.write(tabulate(course_data, headers=headers, tablefmt="grid"))
