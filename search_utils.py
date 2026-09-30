"""
Search Utilities
-----------------
Contains the linear search used to find a student by roll number.
"""


def search_by_roll_no(results, roll_no_to_find):
    """
    Goes through the results one by one (linear search).
    Returns the matching result dictionary, or None if not found.
    """
    for result in results:
        if result["roll_no"] == roll_no_to_find:
            return result
    return None
