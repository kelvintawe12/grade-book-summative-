#!/usr/bin/python3
from tabulate import tabulate
from gradebook import GradeBook
from student import Student
from course import Course

# ANSI escape codes for coloring
HEADER = "\033[1;34m"
OKGREEN = "\033[1;32m"
ENDC = "\033[0m"

def print_menu():
    """Prints the menu options in a structured table format."""
    menu_options = [
        [1, "Add student"],
        [2, "Add course"],
        [3, "Register student grades"],
        [4, "Calculate ranking"],
        [5, "Search by grade"],
        [6, "Generate transcript"],
        [7, "View student list"],
        [8, "View course list"],
        [9, "Update student details"],
        [10, "Exit"]
    ]
    headers = ["ID", "Description"]
    print(f"\n{HEADER}Grade Book Application{ENDC}")
    print(tabulate(menu_options, headers=headers, tablefmt="grid", stralign="center"))

def update_student_details(gradebook):
    """Updates the details of an existing student."""
    email = input("Enter the email of the student to update: ")
    student = gradebook.student_list.get(email)
    if not student:
        print("Student not found.")
        return

    update_options = [
        [1, "Name"],
        [2, "Email"],
        [3, "Courses"],
        [4, "Update Everything"],
        [5, "Cancel"]
    ]
    headers = ["ID", "Description"]
    print(tabulate(update_options, headers=headers, tablefmt="grid", stralign="center"))

    choice = input("Enter your choice: ")
    if choice == "1":
        student.names = input("Enter new name: ")
        print(f"{OKGREEN}Name updated successfully.{ENDC}")
    elif choice == "2":
        new_email = input("Enter new email: ")
        gradebook.student_list[new_email] = gradebook.student_list.pop(email)
        student.email = new_email
        print(f"{OKGREEN}Email updated successfully.{ENDC}")
    elif choice == "3":
        course_name = input("Enter course name: ")
        grade = float(input("Enter grade: "))
        credits = float(input("Enter credits: "))
        student.register_for_course(course_name, grade, credits)
        print(f"{OKGREEN}Course updated successfully.{ENDC}")
    elif choice == "4":
        student.names = input("Enter new name: ")
        new_email = input("Enter new email: ")
        course_name = input("Enter course name: ")
        grade = float(input("Enter grade: "))
        credits = float(input("Enter credits: "))
        gradebook.student_list[new_email] = gradebook.student_list.pop(email)
        student.email = new_email
        student.register_for_course(course_name, grade, credits)
        print(f"{OKGREEN}Student details updated successfully.{ENDC}")
    elif choice == "5":
        print("Update canceled.")
        return

    gradebook.save_data()
    gradebook.update_student_list_file()

def main():
    """Main function to run the Grade Book Application."""
    gradebook = GradeBook()
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            gradebook.add_student(student)
            print(f"{OKGREEN}Student added successfully.{ENDC}")
            gradebook.update_student_list_file()
        
        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = float(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            gradebook.add_course(course)
            print(f"{OKGREEN}Course added successfully.{ENDC}")
            gradebook.update_course_list_file()
        
        elif choice == "3":
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            credits = float(input("Enter credits: "))
            gradebook.register_student_for_course(student_email, course_name, grade, credits)
            print(f"{OKGREEN}Student grades registered successfully.{ENDC}")
            gradebook.update_student_list_file()
        
        elif choice == "4":
            gradebook.calculate_GPA()
            ranked_students = gradebook.calculate_ranking()
            print(f"{HEADER}Student Rankings:{ENDC}")
            table = [[i + 1, student.names, student.email, student.GPA] for i, student in enumerate(ranked_students)]
            headers = ["Rank", "Name", "Email", "GPA"]
            print(tabulate(table, headers=headers, tablefmt="grid", stralign="center"))
        
        elif choice == "5":
            course_name = input("Enter course name: ")
            try:
                lower_grade = float(input("Enter lower grade range: "))
                upper_grade = float(input("Enter upper grade range: "))
            except ValueError:
                print("Invalid input. Please enter numeric values for grade ranges.")
                continue
            students = gradebook.search_by_grade(course_name, (lower_grade, upper_grade))
            print(f"{HEADER}Students with grades in the specified range:{ENDC}")
            for student in students:
                print(f"{student.names} ({student.email})")
        
        elif choice == "6":
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            print(transcript)
        
        elif choice == "7":
            from list_students import display_student_list
            display_student_list()
        
        elif choice == "8":
            from list_courses import display_course_list
            display_course_list()

        elif choice == "9":
            update_student_details(gradebook)
        
        elif choice == "10":
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
