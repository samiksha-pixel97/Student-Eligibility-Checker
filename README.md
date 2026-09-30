# Student Eligibility & Debarment Checker

Every semester, someone has to go through a list of students and work out who is allowed to sit the exams and who isn't. It usually comes down to two things: attendance and internal marks. This project does that job automatically.

It's a command-line program written in Python. You give it student records, and it sorts each student into one of three groups: **Eligible**, **Condonation Required**, or **Debarred**. Then it produces reports for individual students and for the whole class.

I built it for **CSE1021 – Introduction to Problem Solving and Programming**.

## What it can do

- Store student records (roll number, name, attendance %, internal marks)
- Check eligibility using tiered rules for attendance and marks
- Combine both checks into one clear status, like "Debarred - Attendance" or "Condonation Required"
- Give a class summary showing how many students fall into each group
- List debarred students in roll-number order, using a bubble sort I wrote myself
- Look up any student by roll number with a linear search
- Run everything from a simple menu, so there's nothing to memorise

## What it's built with

Just plain Python 3. No external libraries, so there's nothing extra to install.

The project uses the main ideas from the course: conditionals, functions, lists, dictionaries, loops, and hand-written sorting and searching (no built-in shortcuts).

## How the files are organised
Student-Eligibility-Checker
├── main.py # Starts the program and shows the menu
├── student_data.py # Stores and validates student records
├── eligibility_engine.py # The attendance and marks rules
├── report_generator.py # Reports, summary, and saving to a file
├── sorting_utils.py # My bubble sort
├── search_utils.py # Linear search by roll number
├── test_eligibility.py # Tests
├── README.md
├── statement.md
└── *.png # Screenshots used below

## How to run it

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open the folder in your terminal or code editor.
4. Run:
5. Pick an option from the menu (1 to 7). You can view students, add a student, run the evaluation, see the debarred list, search, save a report, or exit.

## Trying it out

If you want to check that everything works, here's a good order to go through:

- **Option 1** shows the sample students that are already loaded.
- **Option 3** runs the full evaluation and shows each student's result plus the class summary.
- **Option 2** lets you add your own student. Run option 3 again and they should appear with the right status.
- **Option 4** lists debarred students. They should be in ascending roll-number order.
- **Option 5** searches for a student. Try a roll number like `21BHI001`.
- **Option 6** saves everything to `eligibility_report.txt` in the project folder.
- **Option 7** exits the program.

To run the tests, use:
python test_eligibility.py

Every line should say `PASS`, and the last line should read `20 passed, 0 failed`.

## Screenshots

### Menu Interface
![Menu](/menu.png)

### Evaluation Output
![Evaluation Output](/evaluation_output.png)

### Generated Report File
![Report File](/report_file.png)

### Test Eligibility
![Pass or Fail statistics](/test_eligibility.png)