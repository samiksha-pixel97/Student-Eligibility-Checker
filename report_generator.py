"""
Module 3: Report Generation & Analytics
------------------------------------------
This file takes the evaluation results and produces readable reports:
- per-student status
- class-wide summary counts
- a filtered list of debarred students
- a text-file export of the report
Sorting and searching live in sorting_utils.py and search_utils.py. """

from eligibility_engine import evaluate_all_students
from sorting_utils import sort_by_roll_no
from search_utils import search_by_roll_no


def print_individual_reports(results):
   
    """ Prints each student's roll number, name, and final status in a clean, readable format. """
    
    print("--- Individual Student Report ---")
    for result in results:
        print(f"{result['roll_no']} | {result['name']:<10} | {result['status']}")


def print_summary(results):
   
    """ Counts how many students fall into each category and prints totals. Uses simple counting logic. """
    eligible_count = 0
    condonation_count = 0
    debarred_count = 0

    for result in results:
        if result["status"] == "Eligible":
            eligible_count += 1
        elif result["status"] == "Condonation Required":
            condonation_count += 1
        else:
            # anything else is some form of "Debarred - ..."
            debarred_count += 1

    print("--- Class Summary ---")
    print("Total Students:", len(results))
    print("Eligible:", eligible_count)
    print("Condonation Required:", condonation_count)
    print("Debarred:", debarred_count)


def get_debarred_students(results):
    
    """ Filters out only the students whose status starts with "Debarred". Returns a new list containing just those students. """
    debarred_list = []
    for result in results:
        if result["status"].startswith("Debarred"):
            debarred_list.append(result)
    return debarred_list


def save_report_to_file(results, filename="eligibility_report.txt"):
   
    """ Writes the full report to a text file, so it can be shared or attached as evidence in the project report. """
    with open(filename, "w") as file:
        file.write("Student Eligibility Report")
        file.write("===========================")
        for result in results:
            file.write(f"{result['roll_no']} | {result['name']} | {result['status']}")
    print(f"Report saved to {filename}")


# Quick test - only runs when this file is executed directly.
if __name__ == "__main__":
    all_results = evaluate_all_students()

    print_individual_reports(all_results)
    print_summary(all_results)

    debarred_students = get_debarred_students(all_results)
    sorted_debarred = sort_by_roll_no(debarred_students)
    print("--- Debarred Students (sorted by roll no) ---")
    for student in sorted_debarred:
        print(student["roll_no"], "-", student["name"])

    found = search_by_roll_no(all_results, "21BHI003")
    print("--- Search Result for 21BHI003 ---")
    if found:
        print(found["roll_no"], "-", found["name"], "->", found["status"])
    else:
        print("Student not found.")

    save_report_to_file(all_results)
