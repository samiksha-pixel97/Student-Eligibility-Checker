""" Module 1: Student Data Management

----------------------------------

This file deals with storing the student data and performing some validation checks on the data passed. Every student is stored in a dictionary and a list is created in order to store all the students records. """



# This is the list of students, containing dictionaries as elements (in practice, this list could be generated based on user input or read from a file)



students = [

    {"roll_no": "21BHI001", "name": "Bunny", "attendance": 82.0, "internal_marks": 45},

    {"roll_no": "21BHI002", "name": "Misbah", "attendance": 60.0, "internal_marks": 30},

    {"roll_no": "21BHI003", "name": "Anushka", "attendance": 68.5, "internal_marks": 38},

    {"roll_no": "21BHI004", "name": "Samanyu", "attendance": 90.0, "internal_marks": 48},

    {"roll_no": "21BHI005", "name": "Rishika", "attendance": 55.0, "internal_marks": 25},

]



def is_valid_student(student):

    """ Checks whether a student's attendance and marks are in the given range or not (attendance between 0-100, internal marks between 0-50). """



    if student["attendance"] < 0 or student["attendance"] > 100:

        return False

    if student["internal_marks"] < 0 or student["internal_marks"] > 50:

        return False

    return True



def add_student(roll_no, name, attendance, internal_marks):

    """ Adds a new student to the list of students, after validating the given inputs. """



    new_student = {

        "roll_no": roll_no,

        "name": name,

        "attendance": attendance,

        "internal_marks": internal_marks,

    }



    if is_valid_student(new_student):

        students.append(new_student)

        print(f"Added student: {name}")

    else:

        print(f"Invalid data for {name} — not added.")



def display_all_students():

    """ Displays the basic information of all the students, this is useful in order to check what data has been stored. """



    for student in students:

        print(student["roll_no"], "-", student["name"],

              "| Attendance:", student["attendance"],

              "| Internal Marks:", student["internal_marks"])



# Performing a quick test of the file (this will only run when we call this file directly, not when importing it into main.py)



if __name__ == "__main__":

    display_all_students()

    add_student("21BHI006", "Gitesh", 72.0, 40)

    print("After adding a new student:")

    display_all_students()