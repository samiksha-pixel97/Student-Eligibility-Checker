# eligibility.py
# Checks each student's attendance and internal marks and decides
# whether they are Eligible, need Condonation, or are Debarred.

from student_data import students

ATTENDANCE_ELIGIBLE = 75      # 75% or more is fine
ATTENDANCE_CONDONATION = 65   # 65-74% needs condonation
MIN_INTERNAL_MARKS = 20       # minimum marks needed in internals


# attendance check
def check_attendance_status(attendance):
    if attendance >= ATTENDANCE_ELIGIBLE:
        return "Eligible"
    elif attendance >= ATTENDANCE_CONDONATION:
        return "Condonation"
    else:
        return "Debarred"


# internal marks check (only two outcomes here)
def check_internal_marks_status(internal_marks):
    if internal_marks >= MIN_INTERNAL_MARKS:
        return "Eligible"
    else:
        return "Debarred"


# combine both results into one final status
def get_combined_status(attendance_status, marks_status):
    if attendance_status == "Eligible" and marks_status == "Eligible":
        return "Eligible"
    elif attendance_status == "Debarred" and marks_status == "Debarred":
        return "Debarred - Attendance & Internals"
    elif attendance_status == "Debarred":
        return "Debarred - Attendance"
    elif marks_status == "Debarred":
        return "Debarred - Internal Marks"
    else:
        # only case left: attendance is in the condonation range
        # and marks are fine
        return "Condonation Required"


# run both checks for one student and return the final status
def evaluate_student(student):
    attendance_status = check_attendance_status(student["attendance"])
    marks_status = check_internal_marks_status(student["internal_marks"])
    return get_combined_status(attendance_status, marks_status)


# go through all students and collect their results in a new list
# (not changing the original list)
def evaluate_all_students():
    results = []
    for student in students:
        status = evaluate_student(student)
        results.append({
            "roll_no": student["roll_no"],
            "name": student["name"],
            "status": status
        })
    return results


# quick test, runs only when this file is run directly
if __name__ == "__main__":
    for result in evaluate_all_students():
        print(result["roll_no"], "-", result["name"], "->", result["status"])