#!/usr/bin/python3
from student import Student
from course import Course

class GradeBook:
    """
    A class to manage student records and course registrations.

    Attributes:
        student_list (list): A list of all students in the grade book.
        course_list (list): A list of all courses available in the grade book.
    """

    def __init__(self):
        """
        Initializes an empty grade book with no students or courses.
        """
        self.student_list = []
        self.course_list = []
    
    def add_student(self, student):
        """
        Adds a new student to the grade book.

        Args:
            student (Student): The student object to be added.
        """
        self.student_list.append(student)
    
    def add_course(self, course):
        """
        Adds a new course to the grade book.

        Args:
            course (Course): The course object to be added.
        """
        self.course_list.append(course)
    
    def register_student_for_course(self, student_email, course_name, grade):
        """
        Registers a student for a course and records their grade.

        Args:
            student_email (str): The email address of the student.
            course_name (str): The name of the course.
            grade (float): The grade received in the course.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        
        if student and course:
            student.register_for_course(course_name, grade, course.credits)
        else:
            print("Student or Course not found.")
    
    def calculate_GPA(self):
        """
        Calculates the GPA for all students in the grade book.
        """
        for student in self.student_list:
            student.calculate_GPA()
    
    def calculate_ranking(self):
        """
        Calculates and returns a ranked list of students based on their GPA.

        Returns:
            list: A list of students sorted by GPA in descending order.
        """
        sorted_students = sorted(self.student_list, key=lambda s: s.GPA, reverse=True)
        return sorted_students
    
    def search_by_grade(self, course_name, grade_range):
        """
        Searches for students who obtained grades within a specific range in a course.

        Args:
            course_name (str): The name of the course.
            grade_range (tuple): A tuple containing the lower and upper bounds of the grade range.

        Returns:
            list: A list of students who obtained grades within the specified range.
        """
        lower, upper = grade_range
        students = [s for s in self.student_list if s.courses_registered.get(course_name, (0, 0))[0] in range(lower, upper+1)]
        return students
    
    def generate_transcript(self, student_email):
        """
        Generates a transcript for a student, showing their GPA and course details.

        Args:
            student_email (str): The email address of the student.

        Returns:
            str: The transcript for the student.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            transcript = f"\033[1;34mTranscript for {student.names} ({student.email}):\033[0m\n"
            transcript += f"\033[1;32mGPA: {student.GPA:.2f}\033[0m\n"
            transcript += "\033[1;36mCourses Registered:\033[0m\n"
            for course, (grade, credits) in student.courses_registered.items():
                transcript += f"Course: {course}, Grade: {grade}, Credits: {credits}\n"
            return transcript
        else:
            return "Student not found."
