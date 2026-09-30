"""
Main Program: Student Eligibility & Debarment Checker
--------------------------------------------------------
This is the entry point of the project. It shows a simple menu and, depending on what the user picks, calls the right function from the other modules. """

from student_data import display_all_students, add_student
from eligibility_engine import evaluate_all_students
from report_generator import (
    print_individual_reports,
    print_summary,
    get_debarred_students,
    save_report_to_file,
)
from sorting_utils import sort_by_roll_no
from search_utils import search_by_roll_no


def show_menu():
    """Just prints out the list of options for the user to pick from."""
    print("===== Student Eligibility & Debarment Checker =====")
    print("1. View all students")
    print("2. Add a new student")
    print("3. Run eligibility evaluation (individual + summary)")
    print("4. View debarred students (sorted by roll no)")
    print("5. Search a student by roll number")
    print("6. Save report to file")
    print("7. Exit")


def main():

    """ Keeps the menu running in a loop and reacts to whatever the user types, until they choose option 7 to exit. """

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_all_students()

        elif choice == "2":
            roll_no = input("Enter roll number: ").strip().upper()
            name = input("Enter name: ").strip()
            # attendance and marks have to be numbers - if the user accidentally types letters,
            # float() will throw a ValueError, so we catch that instead of letting the program crash
            try:
                attendance = float(input("Enter attendance percentage: "))
                internal_marks = float(input("Enter internal marks: "))
            except ValueError:
                print("Invalid input. Attendance and marks must be numbers.")
            else:
                if roll_no == "" or name == "":
                    print("Roll number and name cannot be empty.")
                else:
                    add_student(roll_no, name, attendance, internal_marks)

        elif choice == "3":
            results = evaluate_all_students()
            print_individual_reports(results)
            print_summary(results)

        elif choice == "4":
            results = evaluate_all_students()
            debarred = get_debarred_students(results)
            sorted_debarred = sort_by_roll_no(debarred)
            print("--- Debarred Students (sorted by roll no) ---")
            for student in sorted_debarred:
                print(student["roll_no"], "-", student["name"], "->", student["status"])

        elif choice == "5":
            roll_no = input("Enter roll number to search: ").strip().upper()
            results = evaluate_all_students()
            found = search_by_roll_no(results, roll_no)
            if found:
                print(found["roll_no"], "-", found["name"], "->", found["status"])
            else:
                print("Student not found.")

        elif choice == "6":
            results = evaluate_all_students()
            save_report_to_file(results)

        elif choice == "7":
            print("Exiting. Goodbye!")
            break  # breaks out of the while loop so the program actually ends

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()