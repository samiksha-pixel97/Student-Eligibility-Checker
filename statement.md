# Project Statement

## Student Eligibility & Debarment Checker

### 1. Problem Statement

Determining whether a student is eligible to sit for end-of-semester examinations is a routine yet critical process in academic institutions. In most colleges, eligibility hinges on meeting specific criteria, primarily minimum attendance requirements and internal assessment scores. 

When handled manually across hundreds of students, this process quickly becomes tedious, time-consuming, and prone to human error. A miscalculation can lead to incorrect debarment or mistakenly allowing ineligible students to take an exam.

The **Student Eligibility & Debarment Checker** is a lightweight, Python-based tool designed to automate and simplify this administrative task. By taking basic student information—such as roll number, name, attendance percentage, and internal marks—it automatically evaluates each record against pre-set academic criteria and categorizes students into clear statuses:

* **Eligible**
* **Condonation Required**
* **Debarred**

Beyond standard evaluations, the application includes features for searching student records, sorting debarred students for administrative review, exporting detailed text reports, and generating full class performance summaries.

---

### 2. Aim of the Project

The core objective of this project is to build an efficient, automated Python application that determines exam eligibility using attendance and internal marks. 

In addition to solving a practical problem, the project is designed to demonstrate core computer science principles in a clean, modular format. It applies essential programming concepts including:

* Dynamic user input and validated data types
* Conditional logic and decision-making structures
* Iterative loops and functions
* In-memory storage using lists and dictionaries
* Custom implementation of searching and sorting algorithms
* File I/O operations for report generation
* Modular architecture and unit testing

---

### 3. Key Objectives

1. **Structured Data Management:** Store and manage basic student profile data cleanly in memory.
2. **Input Validation:** Safely accept and validate user inputs to handle invalid entries without program crashes.
3. **Attendance Checks:** Compare student attendance against standard eligibility thresholds and condonation boundaries.
4. **Academic Mark Checks:** Verify whether internal assessment scores meet mandatory cut-offs.
5. **Combined Status Evaluation:** Synthesize attendance and internal marks into a definitive final standing.
6. **Lookup Functionality:** Allow quick single-student searches by roll number.
7. **Organized Debarment Lists:** Display all debarred students in ascending order by roll number.
8. **Exportable Reports:** Save comprehensive eligibility evaluations directly to a readable file.
9. **Class-Wide Summaries:** Provide broad analytical views showing total counts for eligible, condonation-required, and debarred students.
10. **Educational Demonstration:** Highlight practical problem-solving using Python fundamentals learned in introductory programming courses.

---

### 4. Scope & Capabilities

This application is built as an academic evaluation system tailored for departmental or course-level use.

**Supported Features:**
* Add and view student records interactively.
* Evaluate eligibility automatically and pinpoint specific reasons for debarment (e.g., low attendance vs. low internal marks).
* Identify students who fall into the condonation range.
* Perform roll-number lookups.
* Sort debarred student records cleanly.
* Export and save full eligibility reports to disk.
* Display overall class performance statistics.

*Note: The program relies on predefined rules and is meant as an educational tool rather than a full-scale institutional Enterprise Resource Planning (ERP) platform.*

---

### 5. Input Requirements

The program accepts four key data points per student:

* **Roll Number** (Unique identifier)
* **Student Name**
* **Attendance Percentage** (%)
* **Internal Assessment Marks**

All inputs are validated upon entry to ensure numeric inputs fall within expected, realistic bounds.

---

### 6. Processing Pipeline

1. **Data Ingestion:** Collects student identity, attendance figures, and internal marks.
2. **Attendance Evaluation:** Categorizes attendance into standard eligibility, condonation eligibility, or non-eligibility.
3. **Marks Evaluation:** Compares internal scores against the minimum passing threshold.
4. **Status Determination:** Combines both checks to yield final outcomes such as *Eligible*, *Condonation Required*, *Debarred (Attendance)*, or *Debarred (Internal Marks)*.
5. **Output Generation:** Displays individual results and updates aggregate class summaries.

---

### 7. Modular Architecture

To keep the codebase maintainable, readable, and structured, the application is divided into several focused modules:

#### 7.1 Student Data Module (`student_data.py`)
Acts as the data repository. It handles initial student dataset storage and provides helpers for adding and retrieving records.

#### 7.2 Eligibility Engine (`eligibility_engine.py`)
Contains the core business logic. It executes conditional rules to evaluate attendance percentages, mark thresholds, condonation eligibility, and debarment conditions.

#### 7.3 Report Generator (`report_generator.py`)
Formats evaluation results into clean summaries. It formats student records, builds class-level statistics, and handles writing reports out to text files.

#### 7.4 Sorting Module (`sorting_utils.py`)
Implements custom sorting algorithm logic (**Bubble Sort**) to order debarred students sequentially by roll number without relying on Python’s native `.sort()`.

#### 7.5 Searching Module (`search_utils.py`)
Provides efficient lookup capabilities across student records using a classic **Linear Search** implementation.

#### 7.6 Main Application (`main.py`)
Serves as the entry point and user interface. It renders an interactive command-line menu:
1. View all students
2. Add a new student
3. Run eligibility evaluation
4. View sorted debarred list
5. Search student by roll number
6. Save eligibility report
7. Exit


### 8. Expected Output Example

When evaluating a student, the program formats the result clearly:
Roll Number      : 21BHI001
Student Name     : Alex Mercer
Attendance       : 82.0%
Internal Marks   : 25 / 30
Status           : Eligible

If a student fails to meet requirements, the output highlights the exact reasoning (e.g., Debarred - Low Attendance (62%)).

### 9. Data Structures & Algorithms
Data Structures:
Lists: Hold collection records sequentially.
Dictionaries: Represent key-value attributes for individual student profiles.
Strings & Numbers: Handle identification details, names, marks, and analytical tallies.
Algorithms:
Linear Search: Iterates through student lists sequentially to match roll numbers during lookups.
Bubble Sort: Repeatedly steps through the debarred list, comparing and swapping adjacent items to sort roll numbers in ascending order.

#### 10. File Handling & Testing
File Operations: Evaluated results, status breakdowns, and summary counts can be saved directly to a formatted .txt file, ensuring persistent records after program execution.

Automated Testing (test_eligibility.py): Includes dedicated test scripts that test border cases (e.g., exact boundary attendance percentages, failing marks with high attendance) to ensure accurate status assignment.

### 11. Limitations & Future Enhancements
Current Limitations	Planned Future Enhancements
Command-line interface (CLI) only	Modern Graphical User Interface (GUI)
Local memory data storage	Persistent SQLite/MySQL database integration
Hardcoded eligibility rules	Configurable rule sets per course/department
No role-based authorization	Secure authentication for faculty and admins
Manual entry	CSV / Excel file import and export capabilities.

### 12. Conclusion
The Student Eligibility & Debarment Checker effectively automates what is typically a tedious administrative process. By organizing the program into distinct modules and leveraging foundational computer science concepts, it offers a clean, reliable solution for academic eligibility checks while serving as a practical showcase of Python fundamentals for CSE1021 – Introduction to Problem Solving and Programming.