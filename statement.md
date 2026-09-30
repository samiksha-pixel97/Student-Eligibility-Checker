# Project Statement

## Problem Statement
Colleges require students to meet minimum attendance and internal assessment thresholds to be eligible for mid-semester and end-semester examinations. Manually checking every student against multiple, overlapping rules (attendance percentage, internal marks, condonation categories) is slow, repetitive, and prone to human error. This project automates that evaluation process using core programming concepts learned in this course — conditionals, loops, functions, lists, dictionaries, sorting, and searching.

## Scope of the Project
The project covers:
- Storing and validating student records (attendance and internal marks).
- Evaluating each student's eligibility status using tiered, rule-based logic.
- Generating individual and class-wide summary reports.
- Providing sorting (debarred students by roll number) and searching (by roll number) facilities.
- Exporting results to a text file for record-keeping.

The project does not include a graphical user interface, a persistent database, or web-based access — it is a menu-driven command-line application, in line with the scope of an introductory programming course.

## Target Users
Faculty members and academic administration staff who need a quick, automated way to determine which students are eligible, need condonation, or are debarred from examinations based on attendance and internal marks data.

## High-Level Features
- Add and manage student records.
- Evaluate exam eligibility based on:
  - Attendance percentage (Eligible / Condonation Required / Debarred tiers)
  - Internal assessment marks (minimum threshold check)
- Combine both checks into one final status per student.
- Generate a class-wide summary (counts per category).
- Sort debarred students by roll number using a custom bubble sort.
- Search for a student's status by roll number using linear search.
- Save the complete report to a text file.
