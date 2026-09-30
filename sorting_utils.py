"""
Sorting Utilities
------------------
Contains the custom bubble sort used to order student results by roll number.
Written manually (instead of using Python's built-in sort) to demonstrate
the array-sorting technique covered in Unit 5.
"""


def sort_by_roll_no(student_list):
    """
    Sorts a list of student result-dictionaries by roll number
    using bubble sort. Returns the sorted list.
    """
    n = len(student_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_list[j]["roll_no"] > student_list[j + 1]["roll_no"]:
                # Swap the two neighbouring elements
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]
    return student_list
