#!/usr/bin/python3
from gradebook import GradeBook
from student import Student
from course import Course

# ANSI escape codes for coloring
HEADER = "\033[1;34m"
OKGREEN = "\033[1;32m"
OKCYAN = "\033[1;36m"
ENDC = "\033[0m"

def main():
    """
    Main function to run the Grade Book Application.
    """
    gradebook = GradeBook()
    
    while True:
        print(f"\n{HEADER}Grade Book Application{ENDC}")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for course")
        print("4. Calculate ranking")
        print("5. Search by grade")
        print("6. Generate transcript")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            gradebook.add_student(student)
            print(f"{OKGREEN}Student added successfully.{ENDC}")
        
        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            gradebook.add_course(course)
            print(f"{OKGREEN}Course added successfully.{ENDC}")
        
        elif choice == "3":
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(student_email, course_name, grade)
            print(f"{OKGREEN}Student registered for course successfully.{ENDC}")
        
        elif choice == "4":
            gradebook.calculate_GPA()
            ranked_students = gradebook.calculate_ranking()
            print(f"{HEADER}Student Rankings:{ENDC}")
            for student in ranked_students:
                print(f"{student.names} ({student.email}): GPA = {student.GPA:.2f}")
        
        elif choice == "5":
            course_name = input("Enter course name: ")
            lower_grade = int(input("Enter lower grade range: "))
            upper_grade = int(input("Enter upper grade range: "))
            students = gradebook.search_by_grade(course_name, (lower_grade, upper_grade))
            print(f"{HEADER}Students with grades in the specified range:{ENDC}")
            for student in students:
                print(f"{student.names} ({student.email})")
        
        elif choice == "6":
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            print(transcript)
        
        elif choice == "7":
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
