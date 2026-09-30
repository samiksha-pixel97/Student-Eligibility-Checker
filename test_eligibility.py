"""
Validation Tests
-----------------
Simple tests to check that the eligibility rules, validation,
sorting and searching behave correctly, including boundary values.

Run with:  python test_eligibility.py
"""

from eligibility_engine import (
    check_attendance_status,
    check_internal_marks_status,
    get_combined_status,
)
from student_data import is_valid_student
from sorting_utils import sort_by_roll_no
from search_utils import search_by_roll_no

passed = 0
failed = 0

def run_test(test_name, condition):
    """Prints PASS or FAIL for one test and keeps count."""
    global passed, failed
    if condition:
        print("PASS:", test_name)
        passed += 1
    else:
        print("FAIL:", test_name)
        failed += 1

# --- Attendance rule tests (including boundary values) ---
run_test("Attendance 90 -> Eligible", check_attendance_status(90) == "Eligible")
run_test("Attendance 75 (boundary) -> Eligible", check_attendance_status(75) == "Eligible")
run_test("Attendance 74.9 -> Condonation", check_attendance_status(74.9) == "Condonation")
run_test("Attendance 65 (boundary) -> Condonation", check_attendance_status(65) == "Condonation")
run_test("Attendance 64.9 -> Debarred", check_attendance_status(64.9) == "Debarred")
run_test("Attendance 0 -> Debarred", check_attendance_status(0) == "Debarred")

# --- Internal marks rule tests ---
run_test("Marks 45 -> Eligible", check_internal_marks_status(45) == "Eligible")
run_test("Marks 20 (boundary) -> Eligible", check_internal_marks_status(20) == "Eligible")
run_test("Marks 19 -> Debarred", check_internal_marks_status(19) == "Debarred")

# --- Combined status tests ---
run_test("Both fine -> Eligible",
         get_combined_status("Eligible", "Eligible") == "Eligible")
run_test("Condonation + good marks -> Condonation Required",
         get_combined_status("Condonation", "Eligible") == "Condonation Required")
run_test("Low attendance only -> Debarred - Attendance",
         get_combined_status("Debarred", "Eligible") == "Debarred - Attendance")
run_test("Low marks only -> Debarred - Internal Marks",
         get_combined_status("Eligible", "Debarred") == "Debarred - Internal Marks")
run_test("Both low -> Debarred - Attendance & Internals",
         get_combined_status("Debarred", "Debarred") == "Debarred - Attendance & Internals")

# --- Validation tests ---
good = {"roll_no": "T1", "name": "A", "attendance": 80, "internal_marks": 30}
bad_attendance = {"roll_no": "T2", "name": "B", "attendance": 120, "internal_marks": 30}
bad_marks = {"roll_no": "T3", "name": "C", "attendance": 80, "internal_marks": -5}
run_test("Valid student accepted", is_valid_student(good) is True)
run_test("Attendance above 100 rejected", is_valid_student(bad_attendance) is False)
run_test("Negative marks rejected", is_valid_student(bad_marks) is False)

# --- Sorting test ---
unsorted_list = [{"roll_no": "B"}, {"roll_no": "C"}, {"roll_no": "A"}]
sorted_list = sort_by_roll_no(unsorted_list)
run_test("Bubble sort orders roll numbers",
         [s["roll_no"] for s in sorted_list] == ["A", "B", "C"])

# --- Search tests ---
sample_results = [{"roll_no": "X1", "name": "P", "status": "Eligible"}]
run_test("Search finds existing roll number",
         search_by_roll_no(sample_results, "X1") is not None)
run_test("Search returns None for missing roll number",
         search_by_roll_no(sample_results, "ZZ") is None)

print(f"\nResult: {passed} passed, {failed} failed")